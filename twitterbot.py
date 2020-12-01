#
#a general purpose twitter bot class that lets you do common twitter stuff.
#
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
from device import device
import random
import time
package = 'com.twitter.android'

# TODO replace /Users/vai/Projects/
heart = MonkeyRunner.loadImageFromFile("/Users/henry/Documents/GitHub/insta-chess-mobile/heart.png")
red_heart = MonkeyRunner.loadImageFromFile("/Users/henry/Documents/GitHub/insta-chess-mobile/red-heart.png")

class Twitterbot(device):
    def __init__(self,deviceId,model="pixel2", verbose=False):
        super(Twitterbot,self).__init__(deviceId,model,verbose)
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
              "search": (421, 1741),
              "typeBar": (318, 153),
              "home":(262,139),
              "tweets":(110,284),
              "searchClear": (1012,132),
              "firstResult": (684,750),
              "follow": (932,490),
              "back": (230,1857),
              "backToProfile": (65,125),
              "writeComment":(290,1260),
              "notification": (750,1730),
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
        # when ctrl + c is used in the terminal, remove monkey processes on the phones before ending the process
        if(self.verbose):
            print "Connected to device "+deviceId+"."
        self.openTwitter()
        print "connected to twitter"

    heart_x_offset = 655

    def openTwitter(self):
        activity = 'com.twitter.app.main.MainActivity'
        runComponent = package + '/' + activity
        self.device.startActivity(component=runComponent)
        if(self.verbose):
            print "Started twitter."

    def detectLikeButtons(self,like=True):
      image = self.device.takeSnapshot()
      height = 1750
      heart_height = 37
      heart_width = 39
      sub_image = image.getSubImage((643,0,39,height))
      the_heart_image = heart if like else red_heart
      # sub_image.writeToFile("/Users/vai/Projects/insta-chess-mobile/last-scan.png")
      hits = []
      for x in xrange(1,height-heart_height-1):
        heart_test = sub_image.getSubImage((0,x,heart_width,heart_height))
        if(heart_test.sameAs(the_heart_image, .9)):
          hits.append(x)
          x+=40
      print "detected hits at" + str(hits)
      return hits

    def touchLikeButtons(self,likeOrUnlike=True,official=True):
      heart_locations = self.detectLikeButtons(likeOrUnlike)
      for x in xrange(0,len(heart_locations)):
        if(official):
          self.touchPoint([str(self.heart_x_offset+20),str(heart_locations[x]+20)])
          time.sleep(.1)
      #we return the lowest down heart location, or else the bottom of the scrollable area
      return heart_locations if len(heart_locations)>0 else [900]#1342
