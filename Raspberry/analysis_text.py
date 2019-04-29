import re
from music import Music
from audio import Audio
from LED import ControlLED
from analysis import Analysis
from tuling import TuLing
from temperature import Temperature
from face import Face
from news import News
from motor import Motor
class AnalysisText():

    def __init__(self, camera):

        self.OPEN_LED_pattern = '(.*?开.*?灯.*?)|(.*?灯.*?开.*?)'
        self.CLOSE_LED_pattern = '(.*?关.*?灯.*?)|(.*?灯.*?关.*?)'
        self.MUSIC_pattern = '(.*?唱.*?歌.*?)'
        self.TULING_pattern = '(.*?聊.*?天.*?)'
        self.WEATHER_pattern = '(.*?天.*?气.*?)'
        self.PHOTO_pattern = '(.*?拍.*?照.*?)'
        self.TEMPERATURE_pattern = '(.*?室内温度.*?)'
        self.CPU_TEMPERATURE_pattern = '(.*?CPU温度.*?)'
        self.FACE_pattern = '(.*?人脸识别.*?)'
        self.TIME_pattern = '(.*?时间.*?)'
        self.WEIBO_pattern = '(.*?微博热搜.*?)'
        self.OPEN_CURTAIN_pattern = '(.*?打开窗帘.*?)'
        self.CLOSE_CURTAIN_pattern = '(.*?关闭窗帘.*?)'
        self.analysis = Analysis()
        self.music = Music()
        self.audio = Audio()
        self.tuling = TuLing()
        self.controlLED = ControlLED()
        self.face = Face()
        self.news = News()
        self.motor = Motor()
        self.camera = camera
        self.temperature = Temperature(18)
        self.filename = 'temp.wav'

    def open_LED(self):

        self.controlLED.openLED()

    def close_LED(self):

        self.controlLED.closeLED()

    def take_photo(self):

        self.camera.take_photo()

    def open_curtain(self):
        self.motor.forward(0.003, 512)

    def close_curtain(self):
        self.motor.backward(0.003, 512)

    def play_music(self):

        text = '请问你要听什么歌曲'
        self.analysis.get_audio(text, self.filename)
        self.audio.play_audio(self.filename)
        self.audio.record_audio(self.filename)
        text = self.analysis.analysis(self.filename)
        self.music.play_music(text)

    def get_weather(self, text):

        response_text = self.tuling.tuling_chat(text)
        self.analysis.get_audio(response_text, self.filename)
        self.audio.play_audio(self.filename)
        self.audio.record_audio(self.filename)
        response_text = self.analysis.analysis(self.filename)
        response_text = self.tuling.tuling_chat(response_text)
        self.analysis.get_audio(response_text, self.filename)
        self.audio.play_audio(self.filename)

    def tuling_chat(self):

        text = '进入图灵机器人智能聊天模式,开始聊天'
        self.analysis.get_audio(text, self.filename)
        self.audio.play_audio(self.filename)
        while True:
            self.audio.record_audio(self.filename)
            text = self.analysis.analysis(self.filename)
            if text == '退出聊天':
                text = '智能聊天模式已关闭'
                self.analysis.get_audio(text, self.filename)
                self.audio.play_audio(self.filename)
                break
            response_text = self.tuling.tuling_chat(text)
            self.analysis.get_audio(response_text, self.filename)
            self.audio.play_audio(self.filename)

    def get_temperature(self):

        hum, temp = self.temperature.get_temp()
        text = "室内温度" + str(temp) + "度" + "室内湿度" + "百分之" + str(hum)
        self.analysis.get_audio(text, self.filename)
        self.audio.play_audio(self.filename)

    def get_CPU_temperature(self):
        temp = self.temperature.get_CPU_temperature()
        text = "当前CPU温度为" + temp + "度"
        self.analysis.get_audio(text, self.filename)
        self.audio.play_audio(self.filename)


    def face_recognition(self):
        text = "即将开始人脸识别,请将脸对准摄像头"
        self.analysis.get_audio(text, self.filename)
        self.audio.play_audio(self.filename)
        self.camera.take_photo()
        text = self.face.analysis(self.camera.photo_name)
        self.analysis.get_audio(text, self.filename)
        self.audio.play_audio(self.filename)

    def get_time(self):
        date, time = self.temperature.get_time()
        self.analysis.get_audio(date, self.filename)
        self.audio.play_audio(self.filename)
        self.analysis.get_audio(time, self.filename)
        self.audio.play_audio(self.filename)

    def get_weibo_host(self):
        pass

    def send_data(self):
        while True:
            self.temperature.send_data()

    def matching(self, text):

        if text:

            if re.search(self.OPEN_LED_pattern, text):
                self.open_LED()

            elif re.search(self.CLOSE_LED_pattern, text):
                self.close_LED()

            elif re.search(self.MUSIC_pattern, text):
                self.play_music()

            elif re.search(self.WEATHER_pattern, text):
                self.get_weather(text)

            elif re.search(self.TULING_pattern, text):
                self.tuling_chat()

            elif re.search(self.PHOTO_pattern, text):
                self.take_photo()

            elif re.search(self.TEMPERATURE_pattern, text):
                self.get_temperature()

            elif re.search(self.CPU_TEMPERATURE_pattern, text):
                self.get_CPU_temperature()

            elif re.search(self.FACE_pattern, text):
                self.face_recognition()

            elif re.search(self.TIME_pattern, text):
                self.get_time()

            elif re.search(self.WEIBO_pattern, text):
                self.get_weibo_host()

            elif re.search(self.OPEN_CURTAIN_pattern, text):
                self.open_curtain()

            elif re.search(self.CLOSE_CURTAIN_pattern, text):
                self.close_curtain()

            else:
                text = '有点听不懂主人的话,请主人再讲一遍'
                self.analysis.get_audio(text, self.filename)
                self.audio.play_audio(self.filename)
        else:
            text = '主人你没说话呀,你叫我干嘛呢'
            self.analysis.get_audio(text, self.filename)
            self.audio.play_audio(self.filename)


