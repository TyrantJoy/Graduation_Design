#!/usr/bin/python3
import requests
import base64
import json
from urllib.parse import urlencode
from urllib.parse import quote_plus

class Analysis():

    def __init__(self):

        self.FORMAT = 'wav'
        self.RATE = 16000
        self.CHANNEL = 1
        self.API_ASR = 'http://vop.baidu.com/server_api'
        self.API_TTS = 'http://tsn.baidu.com/text2audio'
       # self.TOKEN = '24.69ad1693bb643be206e0eb38d11c0d69.2592000.1552714562.282335-15557520'
        self.CUID = 'RASPBERRY'
        self.DEV_PID = 1536
        self.API_Key = 'bloMxDNlgVv8suLFLq7YumqT'
        self.Secret_Key = 'k8bOR7fwBcBWglrPOBj4re8keZXAxGNi'
        self.CTP = 1
        self.LAN = 'zh'
        self.AUE = 6
        self.PER = 0

    def get_token(self):

        Token_API_Address = 'https://openapi.baidu.com/oauth/2.0/token'
        data = {
            'grant_type' : 'client_credentials',
            'client_id' : self.API_Key,
            'client_secret' : self.Secret_Key,
        }
        result = requests.post(Token_API_Address, data=data)
        response_dict = result.json()
        token = response_dict['access_token']
        return token

    def analysis(self, file_name):

        '''获取token'''
        TOKEN = self.get_token()

        '''读取音频文件'''
        with open(file_name, "rb") as file:
            speech_data = file.read()

        '''计算出音频文件长度'''
        speech_lenth = len(speech_data)

        '''读文件进行base64编码'''
        speech = base64.b64encode(speech_data)
        speech = str(speech, 'utf-8')

        '''初始化json初始字典'''
        data = {
            'format' :self.FORMAT,
            'rate' : self.RATE,
            'channel' : self.CHANNEL,
            'cuid' : self.CUID,
            'token' : TOKEN,
            'dev_pid' : self.DEV_PID,
            'speech' : speech,
            'len' : speech_lenth
        }

        '''将字典格式化成字符串'''
        data_json = json.dumps(data)

        '''设置头部'''
        headers = {
            'Content-Type':'application/json'
        }

        print("------" * 10)
        print("开始分析")
        print("------" * 10)
        result = requests.post(self.API_ASR, data_json, headers)
        response_dict = result.json()
        try:
            result = response_dict['result']
        except Exception as e:
            pass
        else:
            for word in result:
                print(word)
            return result[0]

    def get_audio(self, text, file_name):
        
        token = self.get_token()
        tex = quote_plus(text)
        data = {
            'tex':tex,
            'tok':token,
            'cuid':self.CUID,
            'ctp':self.CTP,
            'lan':self.LAN,
            'aue':self.AUE,
            'per':self.PER
        }

        data_json = urlencode(data)

        result = requests.post(self.API_TTS, data_json)

        with open(file_name, "wb") as file:
            file.write(result.content)
