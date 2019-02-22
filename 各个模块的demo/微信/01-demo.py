import itchat 

class WeChat():

    def __init__(self):
        self.main()

    def main(self):
        @itchat.msg_register(itchat.content.TEXT)
        def text_reply(msg):
            print(msg.text)

        itchat.auto_login(hotReload=True)
        itchat.run()



