from analysis_text import AnalysisText
import itchat
import re
import time
import subprocess
from datetime import datetime
class AnalysisWechatText(AnalysisText):

    def __init__(self, camera):
        AnalysisText.__init__(self, camera)

    def play_music(self, text):

        music_name = text.split()[1]
        response_text = '音乐 %s 正在准备中' % music_name
        itchat.send(response_text, toUserName = 'filehelper')
        self.music.play_music(music_name)

    def get_weather(self, text):

        response_text = text.split()[0]
        response_text = self.tuling.tuling_chat(response_text)
        response_text = text.split()[1]
        response_text = self.tuling.tuling_chat(response_text)
        itchat.send(response_text, toUserName = 'filehelper')

    def get_time(self):
        text = str(datetime.now())
        itchat.send(text, toUserName = 'filehelper')

    def get_temperature(self):
        hum, temp = self.temperature.get_temp()
        text = "室内温度" + str(temp) + "度" + "室内湿度" + "百分之" + str(hum)
        itchat.send(text, toUserName = 'filehelper')

    def get_weibo_hot(self):
        result_dict = self.news.weibo_hot()
        text = ''
        for key, value in result_dict.items():
            temp = key + ":" + value + '\n'
            text += temp
        itchat.send(text, toUserName = 'filehelper')

    def matching(self, text):

        if re.search(self.MUSIC_pattern, text):
            self.play_music(text)

        elif re.search(self.TIME_pattern, text):
            self.get_time()

        elif re.search(self.TEMPERATURE_pattern, text):
            self.get_temperature()

        elif re.search(self.WEATHER_pattern, text):
            self.get_weather(text)

        elif re.search(self.OPEN_LED_pattern, text):
            self.open_LED()

        elif re.search(self.CLOSE_LED_pattern, text):
            self.close_LED()

        elif re.search(self.PHOTO_pattern, text):
            for i in range(3):
                itchat.send(str(3-i), toUserName = 'filehelper')
                time.sleep(1)
            self.take_photo()
            self.audio.play_audio("快门.wav")
            itchat.send_image(self.camera.photo_name, toUserName = 'filehelper')
            subprocess.Popen(['rm', self.camera.photo_name]).wait()

        elif re.search(self.WEIBO_pattern, text):
            self.get_weibo_hot()

        elif re.search(self.OPEN_CURTAIN_pattern, text):
            self.open_curtain()

        elif re.search(self.CLOSE_CURTAIN_pattern, text):
            self.close_curtain()
