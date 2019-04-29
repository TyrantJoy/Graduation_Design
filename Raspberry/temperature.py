import os
import json
import time
from socket import *
import Adafruit_DHT
from database import Database
from datetime import datetime
sensor=Adafruit_DHT.DHT11
database = Database()

class Temperature():

    def __init__(self, gpio):
        self.gpio = gpio

    def get_temp(self):
        humidity, temperature = Adafruit_DHT.read_retry(sensor, self.gpio)
        return humidity, temperature

    def get_time(self):
        date = str(datetime.now().date())
        time = str(datetime.now().time()).split(':')
        hour = time[0]
        minute = time[1]
        second = float(time[2])
        second = str(round(second))
        time = hour + '时' + minute + '分' + second + '秒'
        return date, time

    def get_CPU_temperature(self):
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as file:
            text = file.read()
        temp = float(text) / 1000
        return str(temp)

    def get_CPU_use(self):
        return(str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip()))

    def getRAMinfo(self):
        p = os.popen('free')
        i = 0
        while 1:
            i = i + 1
            line = p.readline()
            if i==2:
                RAM_stats = line.split()[1:4]
                break
        RAM_total = round(int(RAM_stats[0]) / 1000,1)
        RAM_used = round(int(RAM_stats[1]) / 1000,1)
        RAM_free = round(int(RAM_stats[2]) / 1000,1)
        return "Total(MB):" + str(RAM_total) + " Used(MB):" + str(RAM_used) + " Free(MB):" + str(RAM_free)

    def send_data(self):

        info = dict()
        x = list()
        tem = list()
        hum = list()
        light = list()
        ray = list()
        for i in range(5):
            time_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            humi, teme = Adafruit_DHT.read_retry(sensor, 25)
            params = [teme, humi, teme, humi, time_now]
            database.insert(params)
            time.sleep(2)
            x.append(time_now)
            tem.append(teme)
            hum.append(humi)
        info['x'] = x
        info['tem'] = tem
        info['hum'] = hum
        info["CPUUSE"] = self.get_CPU_use()
        info["CPUTEM"] = self.get_CPU_temperature()
        info["RAM"] = self.getRAMinfo()
        x = []
        tem = []
        hum = []
        light = []
        ray = []
        json_dict = json.dumps(info)
        tcp_client_socket = socket(AF_INET, SOCK_STREAM)
        server_ip = '104.243.24.56'
        server_port = 7788
        tcp_client_socket.connect((server_ip, server_port))
        tcp_client_socket.send(json_dict.encode("utf-8"))
        tcp_client_socket.close()

