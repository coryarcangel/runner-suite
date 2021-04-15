from twitterbot import Twitterbot
import time
import random
bot = Twitterbot('FA79F1A04959',"pixel2",True)

bot.scroll(400,800,.1)
time.sleep(1)
bot.scroll(900,100,.1)
total = 0
while(total<10000):
    bot.scroll(900,100,.01)
    total = total + 1
