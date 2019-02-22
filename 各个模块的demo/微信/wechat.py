import itchat
import threading
import time
class WeChat():

    def __init__(self):
        itchat.auto_login()

    def recv_msg(self):
        @itchat.msg_register(itchat.content.TEXT)
        def print_content(msg):
            print("----" * 20)
            if msg.toUserName == 'filehelper':
                text = msg.text
                print(text)

    def send_msg(self):
        itchat.send('Hello, filehelper', toUserName='filehelper')

    def run(self):
        itchat.run()

def test():
    
    @itchat.msg_register(itchat.content.TEXT)
    def print_content(msg):
        print("----" * 20)
        if msg.toUserName == 'filehelper':
            text = msg.text
            print(text)
    itchat.auto_login()
    itchat.run()

    

t = threading.Thread(target=test)
t.start()

while True:
    print("----" * 10)
    time.sleep(2)


