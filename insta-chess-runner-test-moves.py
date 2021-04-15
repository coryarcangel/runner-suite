from device import device 

white = device('R28M421N22Y','username','pword', "arcangel_insta_chess_black",True)
black = device('R28M421MT5B','username','pword',"arcangel_insta_chess_white",True)


white.openInstagram()
black.openInstagram()

for x in xrange(0,25):
    if(x%2 == 0):
        white.makeTestMove(x)
    else: 
        black.makeTestMove(x)
    pass
