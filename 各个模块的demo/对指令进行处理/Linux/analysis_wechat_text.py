from analysis_text import AnalysisText
import itchat
import re
import time
class AnalysisWechatText(AnalysisText):

    def __init__(self):
        AnalysisText.__init__(self)

    def play_music(self, text):
        
        music_name = text.split()[1]
        response_text = '音乐 %s 正在准备中' % music_name
        itchat.send(response_text, toUserName = 'filehelper')
        self.music.play_music(self.audio, music_name)          

    def tuling_chat(self):
        pass

    def get_weather(self, text):
        
        response_text = text.split()[0]
        response_text = self.tuling.tuling_chat(response_text)
        response_text = text.split()[1]
        response_text = self.tuling.tuling_chat(response_text)
        itchat.send(response_text, toUserName = 'filehelper')

    def matching(self, text):

        if re.search(self.MUSIC_pattern, text):
            self.play_music(text)

        elif re.search(self.WEATHER_pattern, text):
            self.get_weather(text)
