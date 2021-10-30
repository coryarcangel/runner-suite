from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
import os
from os import sys, path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from classes.device import device

# Fiddle with these values until you isolate the like button exactly
WIDTH = 63
HEIGHT = 56
X_OFFSET = 37
Y_OFFSET = 1100

print("Connecting to device! Make sure a like button is visible.")
phone = device()
image = phone.device.takeSnapshot()
sub_image = image.getSubImage((X_OFFSET,Y_OFFSET,WIDTH,HEIGHT))  #(643,0,39,height)
sub_image.writeToFile(phone.projectDirectory+"/data/like-button-attempt.png")
print("Saving the attempt to the data folder as like-button-attempt.png")
print("Update these values in classes/instabot.py or classes/twitterbot.py at the top.")
print("Then like the post, and run this script again to get a screenshot of the 'liked' icon.")
