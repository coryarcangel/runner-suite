#
#a general purpose instagram bot class that lets you do common instagram stuff.
#
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage

from device import device
import random
import time
package = 'com.instagram.android'

# Enter values found with utitilies/calibrate_like_buttons.py below!!
CALIBRATE_LIKE_BUTTON_ICON_WIDTH = 63
CALIBRATE_LIKE_BUTTON_ICON_HEIGHT = 57
CALIBRATE_LIKE_BUTTON_ICON_X_OFFSET = 37

class Instabot(device):
    def __init__(self,model, verbose):
        super(Instabot,self).__init__(model,verbose)
        self.heart = MonkeyRunner.loadImageFromFile(self.projectDirectory+"/data/insta-like-unliked.png")
        self.red_heart = MonkeyRunner.loadImageFromFile(self.projectDirectory+"/data/insta-like-liked.png")
        self.heart_height = CALIBRATE_LIKE_BUTTON_ICON_HEIGHT
        self.heart_width = CALIBRATE_LIKE_BUTTON_ICON_WIDTH
        self.heart_x_offset = CALIBRATE_LIKE_BUTTON_ICON_X_OFFSET
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
        # when ctrl + c is used in the terminal, remove monkey processes on the phones before ending the process
        if(self.verbose):
            print "Connected to device "+self.deviceId+"."
        self.openInstagram()

    def openInstagram(self):
        activity = 'com.instagram.mainactivity.MainActivity'
        runComponent = package + '/' + activity
        self.device.startActivity(component=runComponent)
        if(self.verbose):
            print "Started instagram."

    def search(self,account='no_account_provided!'):
        self.device.drag((319,1732),(319,1732),1,300)
        time.sleep(2)
        self.touch("searchClear")
        self.touch("typeBar")
        self.type(account)
        time.sleep(3)
        self.touch("firstResult")
        time.sleep(4)

    def comment(self,text="Nice picture",last=False):
        self.touchCommentButton()# 1550 1665
        time.sleep(5)
        self.type(text.replace(" ","%s"),True)
        time.sleep(2)
        # self.touch("submitComment")
        time.sleep(4)
        self.touch("backToProfile")
        time.sleep(2)

    def chooseRandomPost(self,choice=-1):
        if(self.model=="a30"):
           self.touchPoint((str(30+random.randint(0,970)),str(1390+random.randint(1,650))))
        elif(choice>-1):
            self.touchPoint((str(100+320*(choice % 3)),str(1610)))
            print "choosing at " +str(choice)+ " "+str(320*(choice % 3))
        else:
            #this value is 1610 bc 1600 sometimes tapped right in between posts
            self.touchPoint((str(300*random.randint(1,3)),str(1610)))

    def checkNotification(self):
        self.touch("notification")
        time.sleep(5)

    def touchCommentButton(self,xOffset=0):
        inBlack = False
        image = self.device.takeSnapshot()
        sub_image = image.getSubImage((180,700,20,1200))
        blackList = []
        #Finds the vertical sequence of black and white pixels that match the comment button.
        for x in xrange(10,1200):
            px = sub_image.getRawPixel(1,x)
            #if the current pixel is black
            if(px[1] < 50 and px[2] < 50 and px[3] < 50):
                if not inBlack:
                    blackList.append(x+700)
                inBlack = True
            else:
                inBlack = False
            pass
        target = 0;
        for i in range(len(blackList)-1):
            distanceBetweenBlack = abs(blackList[i+1]-blackList[i])
            # make sure space btw black lines matches comment button. match
            if(abs(distanceBetweenBlack-50))<2 and target == 0:
                print "blacklist entry is "+str(blackList[i])
                abovepx = sub_image.getRawPixel(1,blackList[i]-10-700)
                isWhiteAbove = abovepx[1] > 252 and abovepx[2] > 252 and abovepx[3] > 252
                middlepx = sub_image.getRawPixel(1,blackList[i]-10-700)
                isWhiteInside = middlepx[1] > 252 and middlepx[2] > 252 and middlepx[3] > 252
                underpx = sub_image.getRawPixel(1,blackList[i]-10-700)
                isWhiteUnder = underpx[1] > 252 and underpx[2] > 252 and underpx[3] > 252
                if(isWhiteAbove and isWhiteInside and isWhiteUnder):
                    target = (blackList[i+1]+blackList[i])/2
        if(target == 0):
            self.scroll(770,500)
            time.sleep(1)
            self.touchCommentButton(xOffset)
        print "the target is "+str(target)
        time.sleep(.1)
        if(target != 0):
            self.device.shell("input tap "+str(180+xOffset)+" "+str(target))
            return target

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
      for x in xrange(1,height-self.heart_height-1):
        heart_test = sub_image.getSubImage((0,x,self.heart_width,self.heart_height))
        if(heart_test.sameAs(the_heart_image, .8)):
          hits.append(x)
          x+=40
      print "detected hits at" + str(hits)
      return hits


    def heartScreenshot(self,y):
        image = self.device.takeSnapshot()
        sub_image = image.getSubImage((self.heart_x_offset,y,self.heart_width,self.heart_height))  #(643,0,39,height)
        sub_image.writeToFile(self.projectDirectory+"/data/insta-like-unliked.png")

    def testTouchLikeButtons(self,likeOrUnlike=True,official=True):
      heart_locations = self.testDetectLikeButtons(likeOrUnlike,official)
      print "trying to touch"
      #we return the lowest down heart location, or else the bottom of the scrollable area
      return heart_locations if len(heart_locations)>0 else [900]#1342

    def touchLikeButtons(self,likeOrUnlike=True,official=True):
      heart_locations = self.detectLikeButtons(likeOrUnlike,official)
      time.sleep(.1)
      for x in xrange(0,len(heart_locations)):
        if(official):
          self.touchPoint([str(self.heart_x_offset+5),str(heart_locations[x]+5)])
          time.sleep(.2)
      #we return the lowest down heart location, or else the bottom of the scrollable area
      return heart_locations if len(heart_locations)>0 else [900]#1342
