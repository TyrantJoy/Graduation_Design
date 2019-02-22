from urllib.parse import urlencode
import requests
import json
import subprocess

class Music():

    def __init__(self):
        self.URL = 'http://music.linuxstudy.cn/'
        self.TYPE = 'netease'
        self.PAGE = 1
        self.FILTER = 'name'

    def get_music_url(self, music_name):

        data = {
            'input':music_name,
            'filter':self.FILTER,
            'type':self.TYPE,
            'page':self.PAGE,
        }

        base_data = {
            'name':music_name,
            'type':self.TYPE,
        }

        referer_url = self.URL + '?' + urlencode(base_data)

        headers = {
            'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
            'Host':'music.linuxstudy.cn',
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'Origin':'http://music.linuxstudy.cn',
            'Referer':referer_url,
            'Cookie':'Hm_lvt_bfc6c23974fbad0bbfed25f88a973fb0=1550406512,1550408380,1550409641; Hm_lpvt_bfc6c23974fbad0bbfed25f88a973fb0=1550411026',
            'X-Requested-With':'XMLHttpRequest'
        }

        result = requests.post(self.URL, data=data, headers=headers)

        music_url = result.json()['data'][0]['url']

        return music_url

    def play_music(self, music_name):

        music_url = self.get_music_url(music_name)

        music_data = requests.get(music_url)

        filename = music_name + '.mp3'

        with open(filename, 'wb') as file:
            file.write(music_data.content)

        subprocess.Popen(['mplayer', filename]).wait()

        subprocess.Popen(['rm', filename]).wait()

