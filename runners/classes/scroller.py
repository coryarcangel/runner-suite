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
        print(options)
        super(Instabot,self).__init__(options)
        for key, value in options.iteritems():
            setattr(self, key, value)

        self.heart = MonkeyRunner.loadImageFromFile(self.projectDirectory+self.like)
        self.red_heart = MonkeyRunner.loadImageFromFile(self.projectDirectory+self.unlike)
        heart_size = getImageSize(self.heart)
        self.heart_width = heart_size[0]
        self.heart_height = heart_size[1]
        self.heart_x_offset = self.like_X_offset
        self.tapLocations.update({
            "a30": {
              "search": (300, 2145),
              "typeBar": (300, 151),
              "searchClear": (1003,149),
              "firstResult": (545,450),
              "firstPost" : (200,1050),
              "postComment": (180,1590),
              "submitComment": (983,1287),
              "backToProfile": (65,150),
              "writeComment":(290,1260),
              "notification": (757,2140),
              "firstNotification": (990,587)
            },
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

    def scrollToNextPost(self,scrollAmt=None):
      self.scroll(scrollAmt if scrollAmt else 660,50,.35)
      image = self.device.takeSnapshot()
      final = 0
      whiteJustEnded = False
      whiteStreak = 0
      maxWhiteStreak = 0
      # snapshot of rightmost bar on screen, starting from the likely middle of current image.
      # we've scrolled down 400 which basically guarantees we have revealed the next post
      sub_image = image.getSubImage((1000,0,80,1600))
      sub_image.writeToFile(self.projectDirectory+"/data/last-scan.png")
      for x in xrange(0,1600):
        pixel = sub_image.getRawPixel(65,x)
        isWhite =  pixel[1] >= 254 and pixel[2] >= 254 and pixel[3] >= 254
        # debug line
        # print "y: "+ str(x) + ", " + str(pixel) + "is white: "+str(isWhite) + ", white streak: "+str(whiteStreak)
        if(whiteStreak > 450 and isWhite == False):
          final = x
        if(whiteStreak > maxWhiteStreak):
          maxWhiteStreak = whiteStreak
        if(isWhite == False):
          whiteStreak = 0
        else:
          whiteStreak = whiteStreak + 1
      # scroll the rest of the way
      if(final == 0 and whiteStreak > 450):
        self.scrollToNextPost(200)
      print "whiteStreak"+str(maxWhiteStreak)
      self.scroll(final-210,0)
      return final

    def touchLikeButton(self):
        print "liked"
        return self.touchCommentButton(-60)

    def detectLikeButtons(self,like=True,test=False):
      image = self.device.takeSnapshot()
      height = 1750
      sub_image = image.getSubImage((self.heart_x_offset,0,self.heart_width,height))  #(643,0,39,height)
      the_heart_image = self.heart if like else self.red_heart
      if(not test):
          sub_image.writeToFile(self.projectDirectory+"/data/last-scan.png")
      hits = []
      for y in xrange(1,height-self.heart_height-1):
        heart_test = sub_image.getSubImage((0,y,self.heart_width,self.heart_height))
        if(heart_test.sameAs(the_heart_image, .8)):
          hits.append(y)
          y+=4
      print "detected hits at" + str(hits)
      return hits

