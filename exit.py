from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import sys
import signal
import subprocess

device = None

def execute():
    device = MonkeyRunner.waitForConnection()
    #my code here

def exitGracefully(signum, frame):
    print "Exiting Gracefully..."
    try:
        subprocess.call("adb shell kill -9 $(adb shell ps | grep monkey | awk '{print $2}')", shell=True)
    except Exception, e:
        print(e)
    sys.exit(1)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, exitGracefully)

print(__name__)