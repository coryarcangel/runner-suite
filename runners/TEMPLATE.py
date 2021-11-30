from classes.scroller import Scroller

config = dict(
# Required
	liked= "/data/insta-like-liked.png",
    like_X_offset=37,
# Optional. defaults are listed here.
    unliked= "/data/insta-like-unliked.png",
    verbose= False,
    model= "pixel2",
	DELAY_BEFORE_LIKE=3,
	SCROLL_BELOW_LIKE=100,
	DELAY_AFTER_LIKE=4.5,
	SCROLL_ON_NOT_FOUND=(800,300),
	SCROLL_DURATION_AFTER_LIKE=1,
	SCROLL_DURATION_AFTER_NO_LIKE=1,
	MAX_ATTEMPTS=1000,
    UNLIKE=False
)


bot = Scroller(config)

#Options explained:
# unliked : The filename of the captured like button, in data folder.
# liked : The filename of the captured, pre-liked button, in data folder. Only needed if you want to auto-unlike.
# like_X_offset : The distance from the left of the like buttons. Copy from imagefinder file.
# model : If not using pixel2, you can add code to do special things with that phone. otherwise leave as default.
# DELAY_BEFORE_LIKE : How long to wait on a screen before liking.
# SCROLL_BELOW_LIKE : How far below the lowest like to scroll.
# DELAY_AFTER_LIKE : How long to wait after liking, before scrolling.
# SCROLL_ON_NOT_FOUND : The y points to scroll when no likes found. Default is 800 to 300 which scrolls DOWN!
# SCROLL_DURATION_AFTER_LIKE : After likes have been found, how fast to scroll (seconds)?
# SCROLL_DURATION_AFTER_NO_LIKE : After likes have not been found, how fast to scroll (seconds)?
# MAX_ATTEMPTS : Set a cap to stop the program after x tries. Default is 1000.
# UNLIKE : If you've just liked lots of posts and want to automatically unlike, set this to true.


