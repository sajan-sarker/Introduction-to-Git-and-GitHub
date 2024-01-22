#!/usr/bin/env python3
import psutil

def check_cpu_usage(percent):
	usage = psutil.cpu_percent()
	return usage<percent
if not check_cpu_usage(75):
	print("Error!, CPU is overloaded")
else:
	print("Everything OK!")
