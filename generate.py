#!/usr/bin/env python

"""
data-plot.py: plot the average of every trace file
"""


"""
__author__	= "Sheng Wei"
__copyright__ = "Copyright 2016"
__credits__ = "Sheng Wei"
__email__ = "shengw12@vt.edu"
"""


import urllib2
import sys
import time
#content = urllib2.urlopen("http://www.google.com").read()


"""
low: lower bound of the number of requests per second
up: upper bound of the number of requests per second
"""
def generate(low, up, init_delay, incre):
	flag = 0; # when flag = 0, delay decreases, when flag = 1, delay increases
	#increase_rate = 10 # percentage
	#init_delay = 2
	curr_delay = init_delay


	count = 0

	while 1: #TODO setup a period instead of a infinite loop
		count += 1

		start = time.time()
		time.sleep(curr_delay)
		urllib2.urlopen("http://www.google.com").read() # http request
		end = time.time()
		#print(curr_delay)
		print(1/ (end - start))
		#print(count)

		
		# delay changed
		if (count == 2):
			if (curr_delay != low  and curr_delay != up and flag == 0): # minimum delay is 1
				curr_delay += incre
			elif (curr_delay != low and curr_delay != up and flag == 1):
				curr_delay -= incre
			elif (curr_delay == low and flag == 1):
				flag = 0
				curr_delay += incre
			elif (curr_delay == up and flag == 0):
				flag = 1
				curr_delay -= incre
			count = 0
		

			


generate(1, 5, 1, 1);

