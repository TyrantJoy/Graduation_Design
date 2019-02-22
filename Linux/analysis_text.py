import re 
from music import Music
from audio import Audio
#from LED import ControlLED
from analysis import Analysis
from tuling import TuLing
class AnalysisText():
    
    def __init__(self):

        self.OPEN_LED_pattern = '(.*?开.*?灯.*?)|(.*?灯.*?开.*?)'
        self.CLOSE_LED_pattern = '(.*?关.*?灯.*?)|(.*?灯.*?关.*?)'
        self.MUSIC_pattern = '(.*?唱.*?歌.*?)'
        self.TULING_pattern = '(.*?聊.*?天.*?)'
        self.WEATHER_pattern = '(.*?天.*?气.*?)'
        self.analysis = Analysis()
        self.music = Music()
        self.audio = Audio()
        self.tuling = TuLing()
        self.filename = 'temp.wav'

    def play_music(self):
        
        text = '请问你要听什么歌曲'
        self.analysis.get_audio(text, self.filename)
        self.audio.play_audio(self.filename)
        self.audio.record_audio(self.filename)
        text = self.analysis.analysis(self.filename)
        self.music.play_music(self.audio, text)

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

    def matching(self, text):
    
        if text:

            if re.search(self.MUSIC_pattern, text):
                self.play_music()

            elif re.search(self.TULING_pattern, text):
                self.tuling_chat()

            elif re.search(self.WEATHER_pattern, text):
                self.get_weather(text)

            else:
                text = '有点听不懂主人的话,请主人再讲一遍'
                self.analysis.get_audio(text, self.filename)
                self.audio.play_audio(self.filename)

        else:
            text = '主人你没说话呀,你叫我干嘛呢'
            self.analysis.get_audio(text, self.filename)
            self.audio.play_audio(self.filename)
