from twitterbot import Twitterbot
import time
import random
bot = Twitterbot('FA79F1A04959',"pixel2",True)
scrolled = 0
total = 0
reference = bot.device.takeSnapshot()
current_snapshot = None
profile_page_nav_offset = 255 #on profile page, the top of screen displays profile name
bot.scroll(1569,484,1.2)
while(total<300):
	likeButtons = bot.touchLikeButtons()
	total += len(likeButtons)
	scroll_point = likeButtons[len(likeButtons)-1] #1642 is the highest point u can start scrolling from
	if(likeButtons[0] != 800):
		time.sleep(1)
	bot.scroll(scroll_point,profile_page_nav_offset,scroll_point/750)
	scrolled += scroll_point
	print str(total) + "total likes"
	current_snapshot = bot.device.takeSnapshot()

#bot.scroll(400,600,.5)
time.sleep(2)
bot.touch("tweets")
