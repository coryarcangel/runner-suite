from instabot import Instabot
import time
import random
bot = Instabot('FA7B71A02648',"pixel2",True)

# while(scrolled_distance < 10000):
#     offset = white.touchLikeButton()
#     time.sleep(2)
#     white.scroll(offset,0,2)
#     scrolled_distance += offset
#     time.sleep(3)


shot1 = bot.device.takeSnapshot().getSubImage((0,0,100,100))
shot2 = bot.device.takeSnapshot().getSubImage((100,100,200,200))


while (shot1.sameAs(shot2) == False):
    # bot.touchLikeButton()
    time.sleep(2)
    if(random.random()<.1):
        bot.comment("Nice picture!")
    bot.scrollToNextPost()
    shot1 = bot.device.takeSnapshot()
    shot2 = bot.device.takeSnapshot()
    time.sleep(1)

bot.scroll(300,800,.1)

bot.touch("backToTopPost")
