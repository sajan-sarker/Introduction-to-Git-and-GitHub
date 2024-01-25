#!/usr/bin/env python3

import os
import shutil
import sys

def check_reboot():
	'''Return True if the computer has a pending reboot.'''
	return os.path.exists("/run/reboot-required")

def check_disk_full(disk):
	'''Return True if there isn't enough disk space, False otherwise'''
	du = shutil.disk_useage(disk)
	free = du.free/ du.total * 100
	return  free > 20
def check_disk():
	if check_disk_full('/'):
		print("Error")
	else:
		print("Everything is OK!")
def main():
	if check_reboot():
		print("Pending Reboot")
		sys.exit(1)
	print("Everything is OK!")
	sys.exit(0)
	check_disk()
	
	


main()
