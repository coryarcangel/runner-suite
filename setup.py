import subprocess
home = subprocess.check_output("/bin/echo ~",shell=True).split("\n")[0]
print(home)

device = subprocess.check_output("adb devices",shell=True).split("\n")[1].split("\t")[0]
print(device)
# HOME_DIR=$(echo ~)
# echo $HOME_DIR
# RUNNER_DEVICE=$(cut -f1 $(adb devices | grep -i "\tdevice"))
# "FA7B71A02648  device"
