from wxpy import *

bot = Bot()

bot.file_helper.send("zheshi yitao ssdad ")
bot.file_helper.send("zheshi yitao ssdad ")
bot.file_helper.send("zheshi yitao ssdad ")
bot.file_helper.send("zheshi yitao ssdad ")
bot.file_helper.send("zheshi yitao ssdad ")
@bot.register(bot.file_helper)
def print_others(msg):
    print(msg.text)

bot.join()

