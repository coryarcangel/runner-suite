from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
from runners.classes.device import device

# Fiddle with these values until you isolate the like button exactly
WIDTH = 60
HEIGHT = 53
X_OFFSET = 38
Y_OFFSET = 406

print("Connecting to device! Make sure a like button is visible.")
phone = device()
image = phone.device.takeSnapshot()
sub_image = image.getSubImage((X_OFFSET,Y_OFFSET,WIDTH,HEIGHT))
sub_image.writeToFile(phone.projectDirectory+"/data/found-with-imagefinder.png")
print("Saving the attempt to the data folder as found-with-imagefinder.png")
print("Update these values in classes/instabot.py or classes/twitterbot.py at the top.")
print("Then like the post, and run this script again to get a screenshot of the 'liked' icon.")
