import requests

KEY = 'eaib9i5cav0fiaqa'
UID = 'U6A6138D1E'

URL = 'https://api.seniverse.com/v3/weather/now.json'
UNIT = 'c'
LANGUAGE = 'zh-Hans'
LOCATION = 'ip'

params = {
    'key':KEY,
    'location':LOCATION,
    'language':LANGUAGE,
    'unit':UNIT
}

result = requests.get(URL, params)

print(result.text)
