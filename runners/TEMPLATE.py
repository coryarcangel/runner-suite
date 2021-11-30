from classes.scroller import Scroller

config = dict(
    model= "pixel2",
	unliked= "/data/found-with-imagefinder.png",
	liked= "/data/found-with-imagefinder-liked.png",
	like_X_offset=37,
	DELAY_BEFORE_LIKE=3,
	SCROLL_BELOW_LIKE=100,
	DELAY_AFTER_LIKE=4.5,
	SCROLL_ON_NOT_FOUND=(800,300),
	SCROLL_DURATION_AFTER_LIKE=1,
	SCROLL_DURATION_AFTER_NO_LIKE=1,
	MAX_ATTEMPTS=1000,
)


bot = Scroller(config)


