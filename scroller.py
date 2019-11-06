from instabot import Instabot
import time
import random
bot = Instabot('FA79F1A04959',"pixel2",True)

# while(scrolled_distance < 10000):
#     offset = white.touchLikeButton()
#     time.sleep(2)
#     white.scroll(offset,0,2)
#     scrolled_distance += offset
#     time.sleep(3)


shot1 = bot.device.takeSnapshot().getSubImage((0,0,100,100))
shot2 = bot.device.takeSnapshot().getSubImage((100,100,200,200))
counter = 0

while (shot1.sameAs(shot2) == False or counter > 350):
	time.sleep(3)
	bot.touchLikeButton()
	time.sleep(4.5)
	print("offset is "+ str(bot.scrollToNextPost()))
	shot1 = bot.device.takeSnapshot()
	shot2 = bot.device.takeSnapshot()
	print(str(counter)+" likes")
	counter = counter + 1
bot.scroll(300,800,.1)

bot.touch("backToTopPost")
