from twitterbot import Twitterbot
import time
import random
bot = Twitterbot('FA79F1A04959',"pixel2",True)
scrolled = 0
total = 0
current_snapshot = None
profile_page_nav_offset = 255 #on profile page, the top of screen displays profile name
bot.scroll(1569,484,1.2)
likeOrUnlike = True
while(total<1500):
	next_snapshot = bot.device.takeSnapshot()
	#if we're stuck at an end of scroll try to refresh
	if(total > 0 and current_snapshot.sameAs(next_snapshot, .9)):
		bot.scroll(500,800,.5)
		time.sleep(.5)
		bot.scroll(900,500,.5)
		time.sleep(.5)
	else:
		likeButtons = bot.touchLikeButtons(likeOrUnlike)
		total += len(likeButtons)
		scroll_point = likeButtons[len(likeButtons)-1] #1642 is the highest point u can start scrolling from

		if(likeButtons[0] != 900):
			time.sleep(1)
		bot.scroll(scroll_point,profile_page_nav_offset,scroll_point/700)
		scrolled += scroll_point
		print str(total) + "total likes"
		current_snapshot = next_snapshot

#bot.scroll(400,600,.5)
time.sleep(2)
bot.touch("tweets")
