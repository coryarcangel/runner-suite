from twitterbot import Twitterbot
import time
import random
bot = Twitterbot("pixel2",True)
scrolled = 0
total = 0
reference = bot.device.takeSnapshot()
current_snapshot = None
while(total<1000):
	likeButtons = bot.touchLikeButtons(False)
	total += len(likeButtons)
	scroll_point = likeButtons[len(likeButtons)-1] #1642 is the highest point u can start scrolling from
	time.sleep(.5)
	bot.scroll(scroll_point,0,scroll_point/500)
	scrolled += scroll_point
	print str(total) + "total likes"
	current_snapshot = bot.device.takeSnapshot()

bot.scroll(400,600,.5)
time.sleep(.5)
bot.touch("tweets")
