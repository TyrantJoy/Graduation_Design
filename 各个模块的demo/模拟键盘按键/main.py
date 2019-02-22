from music import Music
import itchat
from pykeyboard import *
from pymouse import *
import itchat
import threading

def main():

    music = Music()
    music_name = input("请问您要听什么歌曲:")
    music.play_music(music_name)

def wechat():

    m = PyMouse()
    k = PyKeyboard()
    
    @itchat.msg_register(itchat.content.TEXT)
    def print_content(msg):
        if msg.toUserName == 'filehelper':
            if msg.text == '大':
                k.tap_key(k.numpad_keys[0])
            elif msg.text == '小':
                k.tap_key(k.numpad_keys[9])
            elif msg.text == '快进':
                k.tap_key(k.parenright)
            elif msg.text == '后退':
                k.tap_key(k.parenleft)
            elif msg.text == '退出':
                itchat.logout()
    itchat.auto_login(enableCmdQR=2)
    itchat.run()

t = threading.Thread(target=wechat)

if __name__ == "__main__":
    t.start()
    main()
