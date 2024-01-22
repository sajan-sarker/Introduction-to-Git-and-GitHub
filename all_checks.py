#!/usr/bin/env python3

import os
import sys

def check_reboot():
	return os.path.exists("/run/reboot-required")

def main():
	if check_reboot():
		print("Pending Reboot")
		sys.exit(1)
	if disk_full():
		print("Disk Full!")
		sys.exit(1)
	print("Everything is OK!")
	sys.exit(0)


main()
