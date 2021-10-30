Arcangel Studio Runner Code Suite
2019-

Google Pixel 2 phones are the best known androids for this suite.
They are 16:9 resolution which matches common TVs.

How to set up runner devices androids on a new computer:
1) Download + install + open android studio   https://developer.android.com/studio/
2) Add monkeyrunner to your path so you can use it in the terminal. Open up a new terminal and paste this in:
echo 'export PATH="~/Library/Android/sdk/tools/bin:$PATH"' >> ~/.bash_profile; echo 'export PATH="~/Library/Android/sdk/platform-tools:$PATH"' >> ~/.bash_profile
To test if this worked, close terminal and open a new window. Enter "monkeyrunner" in the terminal. You should see the following:
10:44:40 E/adb: * daemon not running; starting now at tcp:5037

3) You will also need to install the java SDK
https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html
(This file is also in the work folder/production/components jdk-8u211-macosx-x64.dmg... if you know what this line means, you know.)
4) set up debug mode on phones so they are recognized by adb
https://www.microfocus.com/documentation/silk-test/205/en/silktestclassic-help-en/GUID-BE1EA2BA-EFF2-4B2D-8F09-4BEE0947DFB2.html

5) Plug in phone(s). Open a terminal and type adb devices. You should see something like the following

R28M421MT5B	device
R28M421N22Y	device

These are the codes you will have to swap into the various programs included in this code suite.

6) This means our phones are connected and we can run our script! Navigate to the code folder in terminal and type monkeyrunner insta-chess-runner.py

File descriptions:
utilities
A couple useful programs for handling recordings and debugging
device.py
The Device class with functions to do most actions we need on the device. Every python file relies on this class.
insta-chess-runner.py
Run with monkeyrunner insta-chess-runner.py. Performs an instagram chess match with two connected devices.
insta-profile-scroller.py
Run with monkeyrunner insta-profile-scroller.py. Scrolls down a single profile(finite) and likes every post.
instabot.py
twitter-feed-scroller.py
Run with monkeyrunner twitter-feed-scroller.py. Scrolls down a feed (infinite) and likes every post.
twitter-profile-scroller.py
twitterbot.py
