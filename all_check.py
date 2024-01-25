#!/usr/bin/env python3

import os
import shutil
import sys

def check_reboot():
	'''Return True if the computer has a pending reboot.'''
	return os.path.exists("/run/reboot-required")

def check_disk_full(disk, min_gb, min_percent):
	'''Return True if there isn't enough disk space, False otherwise'''
	du = shutil.disk_useage(disk)
	free = du.free/ du.total * 100
	gigabyte_free = du.free / 2**30
	if free < min_percent or gagabytes_free < min_gb:
		return True
	return  False

def main():
	if check_reboot():
		print("Pending Reboot")
		sys.exit(1)
	if check_disk_full('/', 2, 10):
		print("Disk FUll")
		sys.exit(1)
	print("Everything is OK!")
	sys.exit(0)
	check_disk()

main()
