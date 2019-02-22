import requests
import json
apiKey = '41ec20e16de74df9b36e7b51af3ff712'
userId = 'raspberry'
url = 'http://openapi.tuling123.com/openapi/api/v2'

def tuling_chat(text):

    perception = {
        'inputText':{
            'text':text
        }
    }

    userInfo = {
        'apiKey':apiKey,
        'userId':userId
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
    result = requests.post(url, data=data_json, headers=headers)
    response_dict = json.loads(result.text)
    response_text = response_dict['results'][0]['values']['text']
    print(response_text)

if __name__ == "__main__":
    text = input("请输入:")
    tuling_chat(text)
