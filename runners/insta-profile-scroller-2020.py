from classes.scroller import Scroller
import time
import random
# FA7B71A02648
config = {
    "model": "pixel2",
	"like": "/data/insta-like-unliked.png",
	"unlike": "/data/insta-like-liked.png",
	"like_X_offset": 37
}


bot = Scroller(config)

counter = 0
# if we can make it to the end
while (counter < 300):
	time.sleep(3)
	bot.touchLikeButton()
	time.sleep(4.5)
	bot.scrollToNextPost()
	print("Counter: "+str(counter))
	counter = counter + 1

bot.scroll(300,800,.1)
bot.touch("backToTopPost")
