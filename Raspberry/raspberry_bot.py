import snowboydecoder
import signal
import time
import itchat
import threading
from analysis_text import AnalysisText
from analysis_wechat_text import AnalysisWechatText
from audio import Audio
from analysis import Analysis
from pi_camera import Camera

camera = Camera()
audio = Audio()
analysis = Analysis()
analysis_text = AnalysisText(camera)
analysis_wechat_text = AnalysisWechatText(camera)
file_name = 'temp.wav'
interrupted = False

def wechat_msg_handle():
    @itchat.msg_register(itchat.content.TEXT)
    def print_content(msg):
        print("微信收到消息")
        if msg.toUserName == 'filehelper':
            analysis.get_audio(msg.text, file_name)
            audio.play_audio(file_name)
            if msg.text == '退出':
                itchat.logout()
            else:
                analysis_wechat_text.matching(msg.text)
    itchat.auto_login(enableCmdQR=2)
    itchat.run()

t = threading.Thread(target=wechat_msg_handle)

def signal_handler(signal, frame):
    global interrupted
    interrupted = True

def interrupt_callback():
    global interrupted
    return interrupted

def callbacks():
    global detector

    #语音唤醒后,提示ding两声
    snowboydecoder.play_audio_file()
    snowboydecoder.play_audio_file()

    #关闭sonwboy功能
    detector.terminate()

    #开启语音识别
    audio.record_audio(file_name)
    text = analysis.analysis(file_name)
    analysis_text.matching(text)
    #打开snowboy功能
    wake_up()

def wake_up():

    global detector
    model = 'resources/models/lize.pmdl'
    signal.signal(signal.SIGINT, signal_handler)
    detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
    detector.start(detected_callback=callbacks,
                   interrupt_check=interrupt_callback,
                   sleep_time=0.03)
    detector.terminate()

if __name__ == "__main__":
    t.start()
    wake_up()
