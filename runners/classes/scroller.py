#
#a general purpose instagram bot class that lets you do common instagram stuff.
#
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage

from device import device
import random
import time

def getImageSize(img):
    foundX = False
    foundY = False
    x = 0
    y = 0
    while foundX == False:
    	try:
    		x = x+1
    		img.getRawPixel(x,0)
    	except:
    		foundX = True
    while foundY == False:
    	try:
    		y = y+1
    		img.getRawPixel(0,y)
    	except:
    		foundY = True
    return [x,y]

class Scroller(device):
    def __init__(self,options):
        super(Scroller,self).__init__(options)
        self.DELAY_BEFORE_LIKE = 3
        self.SCROLL_BELOW_LIKE = 100
        self.DELAY_AFTER_LIKE = 4.5
        self.SCROLL_ON_NOT_FOUND = (800,300)
        self.SCROLL_DURATION_AFTER_LIKE = 1
        self.SCROLL_DURATION_AFTER_NO_LIKE = 1
        self.MAX_ATTEMPTS = 1000
        self.UNLIKE = False
        for key, value in options.iteritems():
            setattr(self, key, value)
        if(self.verbose):
            print("Scrolling with these options",options)
        self.heart = MonkeyRunner.loadImageFromFile(self.projectDirectory+self.unliked)
        heart_size = getImageSize(self.heart)
        self.heart_width = heart_size[0]
        self.heart_height = heart_size[1]
        self.heart_x_offset = self.like_X_offset
        self.LIKE_MODE = not self.UNLIKE
        if not self.LIKE_MODE:
            self.red_heart = MonkeyRunner.loadImageFromFile(self.projectDirectory+self.liked)
        self.tapLocations.update({
            "pixel2" : {
              "search": (319, 1732),
              "typeBar": (300, 127),
              "searchClear": (1003,125),
              "firstResult": (545,403),
              "firstPost" : (200,1450),
              "postComment": (180,1590),
              "submitComment": (1005,994),
              "backToProfile": (65,125),
              "writeComment":(290,1260),
              "notification": (750,1730),
              "firstNotification": (773,587),
              "confirmTag": (500,125),
              "emojis" :(324,1717),
              "heartEmoji": (424,1412),
              "emojisTab": (718,1110),
              "textChars": (75,1750),
              "homePage": (980,1733),
              "videoExit": (330,425),
              "backToTopPost" : (220,129),
              "forceBack":(275,1870)
            }
        })
        self.scrollAndLike()

    def detectLikeButtons(self,like=True,test=False):
      image = self.device.takeSnapshot()
      height = 1750
      sub_image = image.getSubImage((self.heart_x_offset,0,self.heart_width,height))  #(643,0,39,height)
      the_heart_image = self.heart if like else self.red_heart
      sub_image.writeToFile(self.projectDirectory+"/data/last-scan.png")
      hits = []
      for x in xrange(1,height-self.heart_height-1):
        heart_test = sub_image.getSubImage((0,x,self.heart_width,self.heart_height))
        # heart_test.writeToFile(self.projectDirectory+"/data/heart-test-"+str(x)+".png")
        if(heart_test.sameAs(the_heart_image, .9)):
          hits.append(x)
          x+=self.heart_height
      return hits

    def touchLikeButtons(self,likeOrUnlike=True,official=True):
      heart_locations = self.detectLikeButtons(likeOrUnlike,official)
      time.sleep(.1)
      for x in xrange(0,len(heart_locations)):
        if(official):
          self.touchPoint([str(self.heart_x_offset+5),str(heart_locations[x]+5)])
          time.sleep(.2)
      #we return the lowest down heart location, or else the bottom of the scrollable area
      return heart_locations[len(heart_locations)-1] if len(heart_locations)>0 else None#1342

    #main loop
    def scrollAndLike(self):
     counter = 0
     # if we can make it to the end
     while (counter < self.MAX_ATTEMPTS):
     	time.sleep(self.DELAY_BEFORE_LIKE)
     	lastLike = self.touchLikeButtons(self.LIKE_MODE)
        if(self.verbose):
            print "last like: y=",lastLike
        time.sleep(self.DELAY_AFTER_LIKE)
        if(lastLike):
            self.scroll(lastLike+self.SCROLL_BELOW_LIKE,0,self.SCROLL_DURATION_AFTER_LIKE)
        else:
            self.scroll(self.SCROLL_ON_NOT_FOUND[0],self.SCROLL_ON_NOT_FOUND[1],self.SCROLL_DURATION_AFTER_NO_LIKE)
        if(self.verbose):
            print "Counter: ",counter
     	counter = counter + 1

     self.scroll(300,800,.1)
     self.touch("backToTopPost")
