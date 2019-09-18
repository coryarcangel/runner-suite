from device import device

# device.press('KEYCODE_HOME','DOWN_AND_UP') 

#samsung galaxy phone codes: R28M421N22Y / R28M421MT5B

white = device('FA79F1A04959', "_kxd._7881","pixel2",True)
black = device('FA7B71A02648',"_kxd._8691","pixel2",True)

gameLength = 46
for x in xrange(0,gameLength-1):
    (white,black)[x % 2 == 0].makeMove(x)
    print "made move "+str(x)
    pass

(white,black)[(-1+gameLength) % 2 == 0].makeMove(x)
white.touch("homePage")
black.touch("homePage")

