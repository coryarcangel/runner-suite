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

6) Only needed once, run ./setup.sh in the terminal. This will tell monkeyrunner our device ID and project folder!

To make a runner (for Tik Tok in this example):

1) Copy runners/TEMPLATE.py to a new file like tiktok-2021.py.
2) Use the image finder script to isolate a like button:
  monkeyrunner imagefinder.py.
3) When you've isolated the like button, rename the liked button image to something like tiktok-like.png. Also make note of the X offset used.
4) Fill out the variables in tiktok-2021.py.
5) Run monkeyrunner runners/tiktok-2021.py.
You should see some liking!!!!

To record a runner:
1) Install AZ Screen Recorder. Open it and start a recording.
2) Perform your runner to your liking.
3) Stop the recording in AZ Screen Recorder. Rotate so top is facing left. Export and make a note of the filename.
4) Use the filename in utilities/copy_file.sh to copy the video directly to your computer!
