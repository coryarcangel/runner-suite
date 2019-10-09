#old samsung galaxy phone codes: R28M421N22Y / R28M421MT5B
from instabot import instabot
from chessgame import accounts, moves

class ChessPlayer(instabot):
	def __init__(self,deviceId,model="pixel2", opponent,verbose=False):
		super().__init__()

	def comment(self,account,text="my move :)",last=False):
        print "commenting "+text
        self.choosePost()
        time.sleep(4)
        self.touchCommentButton()# 1550 1665
        time.sleep(5)
        self.type("@"+account[0:4])
        time.sleep(1)
        self.touch("confirmTag")
        time.sleep(.2)
        self.type(text.replace(" ","%s"),True)
        time.sleep(2)
        if(last == True):
            self.typeHeartEmoji();
        self.touch("submitComment")
        time.sleep(4)
        self.touch("backToProfile")
        time.sleep(2)

    def makeMove(self,account,move,final):
        if(moveCount != 0):
            self.checkNotification()
        self.search(account)
        self.comment(account,move, final)


white = device('FA79F1A04959', "__kxd._7881","pixel2",True)
black = device('FA7B71A02648',"__kxd._8691","pixel2",True)

for x in xrange(0,len(moves)):
    (white,black)[x % 2 == 0].makeMove(accounts[x],moves.pop(0), len(moves) == 0)
    print "made move "+str(x)

white.touch("homePage")
black.touch("homePage")

