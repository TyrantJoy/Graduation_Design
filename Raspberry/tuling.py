import requests
import json


class TuLing():

    def __init__(self):
        self.APIKEY = '41ec20e16de74df9b36e7b51af3ff712'
        self.USERID = 'raspberry'
        self.URL = 'http://openapi.tuling123.com/openapi/api/v2'

    def tuling_chat(self, text):

        perception = {
            'inputText':{
                'text':text
            }
        }

        userInfo = {
            'apiKey':self.APIKEY,
            'userId':self.USERID
        }

        data = {
            'reqType':0,
            'perception':perception,
            'userInfo':userInfo
        }

        headers = {
            'Content-Type':'application/json'
        }

        data_json = json.dumps(data).encode('utf-8')
        result = requests.post(self.URL, data=data_json, headers=headers)
        response_dict = json.loads(result.text)
        response_text = response_dict['results'][0]['values']['text']
        return response_text




