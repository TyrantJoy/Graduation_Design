#!/usr/bin/python3
import requests
import base64
import json
from urllib.parse import urlencode
from urllib.parse import quote_plus

class Face():

    def __init__(self):

        self.API_Key = 'Svi69GGOrWCGxwGr2G6bd6Xk'
        self.Secret_Key = 'bVd4sB8rYdcWKlAU2b2TX4fdkSBRhsPN'
        self.API_FACE = 'https://aip.baidubce.com/rest/2.0/face/v3/search'
        self.IMAGE_TYPE = 'BASE64'
        self.FACE_TYPE = 'LIVE'
        self.QUALITY_CONTROL = 'LOW'
        self.LIVENESS_CONTROL = 'NORMAL'
        self.GROUP_ID_LIST = 'raspberry'
        self.NAME = {
                'tianchao':'田超',
                'chenglongfei':'程龙飞',
                'lize':'李泽',
                'wangtianlei':'王天磊',
                'yinjun':'殷珺'
                }
    def get_token(self):

        Token_API_Address = 'https://aip.baidubce.com/oauth/2.0/token'
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

        TOKEN = self.get_token()
        request_url = self.API_FACE + "?access_token=" + TOKEN
        with open(file_name, "rb") as file:
            photo_data = file.read()
            photo = base64.b64encode(photo_data)
            photo = str(photo, 'utf-8')

        data = {
            'image':photo,
            'image_type':self.IMAGE_TYPE,
            'face_type':self.FACE_TYPE,
            'group_id_list':self.GROUP_ID_LIST,
            'quality_control':self.QUALITY_CONTROL,
            'liveness_control':self.LIVENESS_CONTROL
        }

        data_json = json.dumps(data)

        headers = {
            'Content-Type':'application/json'
        }

        print("------" * 10)
        print("开始分析")
        print("------" * 10)

        result = requests.post(request_url, data_json, headers)
        result = result.json()
        if result['result']:
            name = result['result']['user_list'][0]['user_id']
            text = '识别成功,当前用户为' + self.NAME[name]
        else:
            text = '识别失败'
        return text

