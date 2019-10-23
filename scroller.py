from instabot import Instabot
import time
scrolled_distance = 0
white = Instabot('FA7B71A02648',"pixel2",True)

while(scrolled_distance < 10000):
    offset = white.touchLikeButton()
    time.sleep(2)
    white.scroll(offset,0,2)
    scrolled_distance += offset
    time.sleep(3)
