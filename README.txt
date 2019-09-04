How to set up instagram chess bot androids on a new computer:
1) Download + install + open android studio
2) Download + install + open android file transfer as well
3) Add /Users/henry/Library/Android/sdk/platform-tools and /Users/henry/Library/Android/sdk/tools.bin to your path. one way to do this is edit ~/.bash_profile(on mac) and add this somewhere in it:

export PATH="$PATH:/Users/[your user name]/Library/Android/sdk/tools/bin"
export PATH="$PATH:/Users/[your user name]/Library/Android/sdk/platform-tools"

4) You will also need to install java SDK
https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html
This file is in the work folder/production/components jdk-8u211-macosx-x64.dmg

** set up debug mode on phones so they are recognized by adb

5) Plug in phones. Open a terminal and type adb devices. You should see the following

R28M421MT5B	device
R28M421N22Y	device

6) This means our phones are connected and we can run our script! Go to the code folder and type monkeyrunner runner.py