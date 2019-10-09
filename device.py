from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
import time
import sys
import random
import signal
import subprocess

package = 'com.instagram.android'

class device():
    def __init__(self,deviceId,model="pixel2", verbose=False):
        self.deviceId = deviceId
        self.model = model
        self.verbose = verbose
        self.device = MonkeyRunner.waitForConnection(3000,deviceId)
        self.tapLocations =  {}
        # when ctrl + c is used in the terminal, remove monkey processes on the phones before ending the this process
        signal.signal(signal.SIGINT, self.exitGracefully)
        if(self.verbose):
            print "Connected to device "+deviceId+"."

    def touch(self,name, touchType="DOWN_AND_UP"):
        self.device.shell("input tap "+str(self.tapLocations[self.model][name][0])+" "+str(self.tapLocations[self.model][name][1]))

    def touchPoint(self,point):
        self.device.shell("input tap "+str(point[0])+" "+str(point[1]))

    def sleep(self,amt):
        time.sleep(amt)

    def type(self,text,slow=False):
        if(slow):
            text = text.replace("%s"," ")
            for letter in text:
                self.device.shell('input text "'+letter+'"')
        else:
            self.device.shell('input text "'+text+'"')
        if(self.verbose):
            print "Typed "+text+"."
    
    def scrollY(self,start,end,duration=1):
        self.device.drag ((500,start),(500,end),duration,300)
        if(self.verbose):
            print "Scrolled from y="+str(start)+" to y="+str(end)
        return


    def typeHeartEmoji(self):
            self.type(" ")
            self.touch("emojis")
            time.sleep(2)
            self.touch("heartEmoji")
            time.sleep(2)
            self.touch("textChars")
            time.sleep(1)

    def exitGracefully(self, signum, frame):
        # Kill monkey on the device or future connections will fail
        print "Exiting Gracefully..."
        try:
            subprocess.call("adb -s "+self.deviceId+" shell kill -9 $(adb -s "+self.deviceId+" shell ps | grep monkey | awk '{print $2}')", shell=True)
        except Exception, e:
            print(e)
        sys.exit(1)