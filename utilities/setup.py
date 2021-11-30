import subprocess
import os

home = subprocess.check_output("/bin/pwd",shell=True).split("\n")[0]
device = subprocess.check_output("adb devices",shell=True).split("\n")[1].split("\t")[0]

print("class Config():")
print("\tdef __init__(self):")
print('\t\tself.deviceId = "'+device+'"')
print('\t\tself.projectDirectory = "'+home+'"')
