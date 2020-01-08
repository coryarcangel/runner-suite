from instabot import Instabot
import time
import random
bot = Instabot('FA79F1A04959',"pixel2",True)

bot.chooseRandomPost()
time.sleep(4)
bot.touchCommentButton()
time.sleep(5)

time.sleep(2)
if(last == True):
    bot.typeHeartEmoji();
bot.touch("submitComment")
time.sleep(4)
bot.touch("backToProfile")
time.sleep(2)

bot.comment("hello!!", True)
