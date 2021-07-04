#!/usr/bin/env python3
import subprocess
import time
import sys
import os
interface = input("Enter interface name: ")
if ";" in interface:
    print("ErroR ;(   dont use ;")
    sys.exit()
else:
    pass
if interface == "--exit":
    sys.exit()
else:
    pass

if interface == "-e":
    sys.exit()
else:
    pass
mac = input("Enter new mac address: ")
if mac == "--exit":
	sys.exit()
else:
	pass
print("\n>> CHanging Mac-Address for {0} To {1}".format(interface,mac))
time.sleep(5)

subprocess.call("ifconfig " + interface + " down",shell=False)
subprocess.call("ifconfig " + interface + " hw ether" + mac,shell=False)
subprocess.call("ifconfig " + interface + " up",shell=False)
print("[+]Done")
time.sleep(5)
os.system("clear")

print("[+]Now Your Mac-Address Is {0}".format(mac))
subprocess.call("ifconfig",shell=True)