# -*- coding: utf-8 -*-

# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
import time
import sys
import random
import signal
import subprocess

timeout = 3000
package = 'com.instagram.android'
accounts = ["arc_chess_slash","arc_chess_vai","arc_chess_axl","arcangel_insta_chess_black","arcangel_insta_chess_white"]
accounts = ["millionaire_mentor","guyfieri","piersmorgan","billmaher","makeupaoa","glowrecipe","earth","glossier","thisisbillgates","tigerwoods","taylorswift","officialspikelee","mohamedbinzayed","speakerpelosi","nytimes","ambaliving","iquitsugar","deliciouslyella","snake.wild","yankees","disney","newtgingrich","leadervladimirputin","generalelectric","ivankatrump","bundeskanzlerin","franciscus","reductress","ikeausa","katyperry","theonion","burgersbae","pitbull","daquan","eminem","jeff_seid","ladyantebellum","thomasrhettakins","billyraycyrus","world_record_egg","icet","danaperino","smoothiebowls","shanedawson","tanamongeau","jakepaul","jaycutler","kristincavallari","allbirds","kfc","loveandlemons","alisoneroman","dollyoatmeal","tulsigabbard","oliviapalermo","xychelsea87","edwardsnowdenofficial","jerrygagosian","adamsandler","hillaryclinton","zuck","therock","awkwafina","alexhonnold","mistyonpointe","kaisafit","hannahbronfman","sjanaelise","eddiehallwsm","vp","beyonce","jimmykimmel","diet_prada","chaninicholas","ocasio2018","nike","ecogoddess","toto_ddung_ee","yogitea","burgerking","tjmaxx","abercrombie","foxnews","tuckercarlsontonight","cnn,","jordanpeele","horsecontent","loveandlemons","alisoneroman","dollyandoatmeal","tulsigabbard","aimeesong","oliviapalermo","xychelsea87","jerrygagosian","fuckjerry","xeniadunkinindia","wendys","panerabread","hypebeast","marianodivaio","breadfaceblog","kanyesundayservices","justinbieber","kimkardashian","marniethedog","chiaraferragnicollection","adrianalimia","zoella","larenconrad","therock","pieraluisa","bichon_tori","michelleobama","glennbeck","weworewhat","travisscott","selenagomez","tinykitchentm","mariekondo","tomilahren","kyliejenner","kayla_itsines","iamcardib"]
accounts = ["millionaire_mentor","guyfieri","piersmorgan","billmaher","makeupaoa","glowrecipe","earth","glossier","thisisbillgates","tigerwoods","taylorswift","mohamedbinzayed","speakerpelosi","nytimes","ambaliving","deliciouslyella","yankees","disney","newtgingrich","leadervladimirputin","generalelectric","ivankatrump","bundeskanzlerin","franciscus","ikeausa","katyperry","burgersbae","pitbull","eminem","jeff_seid","ladyantebellum","thomasrhettakins","billyraycyrus","danaperino","smoothiebowls","shanedawson","tanamongeau","jakepaul","jaycutler","kristincavallari","allbirds","kfc","loveandlemons","alisoneroman","tulsigabbard","oliviapalermo","adamsandler","hillaryclinton","zuck","therock","kaisafit","sjanaelise","eddiehallwsm","vp","jimmykimmel","ocasio2018","nike","yogitea","burgerking","tjmaxx","abercrombie","foxnews","tuckercarlsontonight","cnn","tulsigabbard","oliviapalermo","wendys","panerabread","hypebeast","marianodivaio","justinbieber","kimkardashian","marniethedog","zoella","laurenconrad","therock","pieraluisa","bichon_tori","michelleobama","glennbeck","weworewhat","selenagomez","mariekondo","kyliejenner","kayla_itsines","iamcardib","tifforelie","redskins","raiders","packers","steelers","lakers","chicagobulls","orlandomagic","kingjames","martingarrix","davidguetta","avicii","swedishhousemafia","garthbrooks","dunkin","crackerbarrel","louiselinton/?","lindsaylohan","pashaclubofficial","burgerking","baskinrobbins","siemens","equinox","saudi_aramco","conocophillips","exxonmobil","kochindustriesinc","ted","equinor","jack_astors","hooters","nascar","hollywoodreporter","carrottoplive","britneyspears","diddy","bwwings","shakeshack","amazon","apple","applebees","appletv","netflix","ford","bmw","shaniatwain","norwegiancruiseline","carnival","jeffkoons","buzzfeedtasty","teslamotors","nypost","#hotgirlsummer","#squadgoals","#setlife","#vanlife","#earth","#foodporn","#sunset","#blessed","#dunk"]
moves = ["f3","Nf6","a4","e6","Nc3","c6","Kf2","Qb6+","d4","checkmate"]
moves = ["f3","Nf6","a4","e6","Nc3","c6","Kf2","Qb6+","d4","Be7","Qd3","h5","Bd2","Qxb2","Re1","a5","Nd1","Qb6","Be3","Qb4","c3","Qxa4","Nb2","Qb3","d5","Qxb2","dxe6","dxe6","Nh3","Rg8","Bf4","Qb6+","Kg3","h4+","Kxh4","Nh7+","Kg3","f5","Bxb8","Rxb8","Qd1","Qe3","Qa4","Qe5+","f4","Qe3#"]
random.shuffle(accounts)
class device():
    def __init__(self,deviceId, opponent,model="pixel2", verbose=False):
        self.deviceId = deviceId
        self.opponent = "@"+opponent
        self.model = model
        self.verbose = verbose
        self.device = MonkeyRunner.waitForConnection(timeout,deviceId)
        self.tapLocations =  {
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
              "emojis" :(345,1716),
              "heartEmoji": (991,1368),
              "textChars": (75,1750),
              "homePage": (980,1733),
              "videoExit": (330,425),
              "forceBack":(275,1870)
	        }
        }
        signal.signal(signal.SIGINT, self.exitGracefully)
        if(self.verbose):
            print "Connect to device "+deviceId+"."
        self.openInstagram()
    def exitGracefully(self, signum, frame):
        # Kill monkey on the device or future connections will fail
        print "Exiting Gracefully..."
        try:
            subprocess.call("adb -s "+self.deviceId+" shell kill -9 $(adb -s "+self.deviceId+" shell ps | grep monkey | awk '{print $2}')", shell=True)
        except Exception, e:
            print(e)
        sys.exit(1)
    def confirmPostsView():
        #look for grey bar at top of screen maybe?
        return

    def openInstagram(self):
        activity = 'com.instagram.mainactivity.MainActivity'
        runComponent = package + '/' + activity
        self.device.startActivity(component=runComponent)
        if(self.verbose):
            print "Started instagram."

    def checkAlerts(self):
        return
    def sleep(self,amt):
        time.sleep(amt)
    def scrollY(self,start,end,duration=1):
        self.device.drag ((500,start),(500,end),duration,300)
        if(self.verbose):
            print "Scrolled from y="+str(start)+" to y="+str(end)
        #remember to go back after the comment to see the pic maybe
        return
    def touchPoint(self,point):
    	self.device.shell("input tap "+str(point[0])+" "+str(point[1]))

    def search(self,account='somethin idk'):
        self.sleep(2)
        self.touch("typeBar")
        self.sleep(2)
        self.touch("searchClear")
        self.type(account)
        self.sleep(3)
        self.touch("firstResult")
        self.sleep(4)
    def choosePost(self):
        if(self.model=="a30"):
    	   self.touchPoint((str(30+random.randint(0,970)),str(1390+random.randint(1,650))))
        else:
            self.touchPoint((str(300*random.randint(1,3)),str(1610))) #this value is 1610 bc 1600 sometimes went between links to posts.
    def comment(self,text="my move :)",last=False):
        self.choosePost()
        time.sleep(4)
        self.touchCommentButton()# 1550 1665
        time.sleep(5)
        self.type("@_")
        time.sleep(.5)
        self.touch("confirmTag")
        time.sleep(.2)
        self.type(text.replace(" ","%s"),True)
        time.sleep(2)
        if(last == True):
            self.typeHeartEmoji();
        # self.touch("submitComment")
        time.sleep(4)
        if(last == True):
            self.touch("backToProfile")
            time.sleep(1)
        else:
            self.touch("backToProfile")
            time.sleep(1)
        time.sleep(1)

    def checkNotification(self):
        self.touch("notification")
        time.sleep(2)
        self.touch("firstNotification")
        time.sleep(6.5)
        if(self.model=="a30"):
            self.scrollY(500,2000,.1)
        self.touch("backToProfile")
        time.sleep(1.5)
        self.touch("videoExit")
        time.sleep(.5)
        self.touch("forceBack")
        time.sleep(1)
        black.device.drag ((319,1732),(319,1732),1,300)
        time.sleep(1)

    def home(self):
        self.device.press('KEYCODE_HOME','DOWN_AND_UP')
    def type(self,text,slow=False):
        if(slow):
            text = text.replace("%s"," ")
            for letter in text:
                self.device.shell('input text "'+letter+'"')
        else:
            self.device.shell('input text "'+text+'"')
        if(self.verbose):
            print "Typed "+text+"."
    def typeHeartEmoji(self):
        self.type(" ")
        self.touch("emojis")
        time.sleep(2)
        self.touch("heartEmoji")
        time.sleep(2)
        self.touch("textChars")
        time.sleep(1)

    def touch(self,name, touchType="DOWN_AND_UP"):
        self.device.shell("input tap "+str(self.tapLocations[self.model][name][0])+" "+str(self.tapLocations[self.model][name][1]))
        if(self.verbose):
            print "Tapped "+name+" with "+touchType+"."
    def makeMove(self,moveCount):
        if(moveCount != 0):
            self.checkNotification()
        self.search(accounts.pop())
        self.comment(moves.pop(0))
    def makeFinalMove(self,moveCount):
        self.checkNotification()
        self.touch("backToProfile")
        time.sleep(1)
        self.search(accounts.pop())
        self.comment(moves.pop(0),True)
        self.touch("homePage")

    def makeTestMove(self,moveCount):
        self.search(accounts.pop())
        self.comment("test",True)

    def touchCommentButton(self):
        inBlack = False
        image = self.device.takeSnapshot()
        sub_image = image.getSubImage((180,500,20,1400))
        blackList = []
        # sub_image = image.getSubImage((55,starter,80,80))
        for x in xrange(4,1400):
            # white.device.shell("input tap 200 "+str(starter))
            px = sub_image.getRawPixel(1,x)
            #if its black
            if(px[1] < 50 and px[2] < 50 and px[3] < 50):
                if not inBlack:
                    blackList.append(x+500)
                inBlack = True
            else:
                inBlack = False
            pass
        target = 0;
        for i in range(len(blackList)-1):
            distanceBetweenBlack = abs(blackList[i+1]-blackList[i])
            if(abs(distanceBetweenBlack-50))<2 and target == 0:
                print "blacklist entry is "+str(blackList[i])
                abovepx = sub_image.getRawPixel(1,blackList[i]-10-500)
                isWhiteAbove = abovepx[1] > 250 and abovepx[2] > 250 and abovepx[3] > 250
                middlepx = sub_image.getRawPixel(1,blackList[i]-10-500)
                isWhiteInside = middlepx[1] > 250 and middlepx[2] > 250 and middlepx[3] > 250
                underpx = sub_image.getRawPixel(1,blackList[i]-10-500)
                isWhiteUnder = underpx[1] > 250 and underpx[2] > 250 and underpx[3] > 250
                if(isWhiteAbove and isWhiteInside and isWhiteUnder):
                    target = (blackList[i+1]+blackList[i])/2
        if(target == 0):
            self.scrollY(770,500)
            time.sleep(1)
            self.touchCommentButton()
        print "the target is "+str(target)
        time.sleep(.1)
        if(target != 0):
            self.device.shell("input tap "+str(180)+" "+str(target))  

