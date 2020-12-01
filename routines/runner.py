#old samsung galaxy phone codes: R28M421N22Y / R28M421MT5B
from device import device

white = device('FA79F1A04959', "__kxd._7881","pixel2",True)
black = device('FA7B71A02648',"__kxd._8691","pixel2",True)

for x in xrange(0,white.gameLength):
    (white,black)[x % 2 == 0].makeMove(x)
    print "made move "+str(x)

white.touch("homePage")
black.touch("homePage")

