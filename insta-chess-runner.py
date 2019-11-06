#
# creates two special chess instabots, and uses accounts and moves
# to perform a match.
#

import time
from instabot import Instabot
from chessgame import accounts, moves
INITAL_MOVE_COUNT = len(moves)

class ChessPlayer(Instabot):
	def __init__(self,deviceId, opponent,moves,model="pixel2",verbose=False):
		super(ChessPlayer,self).__init__(deviceId,model,verbose)
		self.opponent = opponent
	# overrides comment method to send comment @ opponent and pull next move.
	def comment(self,text="my move :)",last=False):
		self.chooseRandomPost()
		time.sleep(4)
		self.touchCommentButton()
		time.sleep(5)
		self.type("@"+self.opponent[0:4])
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
		pass

	def makeMove(self):
		if(len(moves) != INITAL_MOVE_COUNT):
			self.checkNotification()
		self.search(accounts.pop())
		print "moves: " + str(len(moves))
		self.comment(moves.pop(0), len(moves) == 0)
		pass

white = ChessPlayer('FA79F1A04959', "__kxd._7881",moves,"pixel2",True)
black = ChessPlayer('FA7B71A02648',"__kxd._8691",moves,"pixel2",True)

for x in xrange(0,INITAL_MOVE_COUNT):
    (white,black)[x % 2 == 0].makeMove()

#end of game

(white,black)[INITAL_MOVE_COUNT % 2 == 0].checkNotification()
white.touch("homePage")
black.touch("homePage")
