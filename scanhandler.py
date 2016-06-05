#!/usr/bin/python
#This file is (soon!) to be launched by displayer and handle the scan threads
import threading, sys, time, random, os
from threadedscan import Scanner
from requests import get
from Queue import Queue
# from pympler import muppy, summary #Memory leak tracker, remove once debugued
# from pympler import refbrowser
class Scanthreader():
	def threader(self,):
		# def output_function(o):
			# return str(type(o))
		# ib = refbrowser.InteractiveBrowser(root)
		# ib.main()
		q = Queue()
		processq = Queue(maxsize=4)
		strq = str(processq)
		print len(strq)
		num_threads = 4
		threads = []
		publicip = get('https://api.ipify.org').text # The result is unicode
		publicip = str(publicip) #Not unicode anymore!
		listpublicip = publicip.split('.')
		print 'My public ip is : ' + publicip
		#print dir(threadedscan)
		mythreadedscan = Scanner()
		myip = listpublicip[0] + '.' + listpublicip[1] + '.' + listpublicip[2] + '.'
		myip = str(myip)
		range1 = 1
		range2 = 254
		b = []
		firstgroup = []
		secondgroup = []
		thirdgroup = []	
		fourthgroup = []
		sleeptime = 0
		qq = {}
		peers = {}
		#peers = {'340d85eab379e5dad0bde7a41672a4b6': '212.83.136.107'}
		runs = 0
		firsttime = 0
		i = 0
		#qq = ()
		for num in xrange (1, 127):
			firstgroup.append(num)
			#print 'mange ton for first group'
		for num in xrange (128, 256):
			secondgroup.append(num)
			#print 'mange ton for second group'
		for num in xrange (1, 256):
			thirdgroup.append(num)
			#print 'mange ton for third group'
		#print type(listpublicip[2])
		while len(peers) < 5:
			while i > 100: #Still not perfect, i falls way under 100
			#while 100 <= i <= 127:
				#print 'je join'
				threadhandler.join
				i = threading.enumerate()
				#print i
				i = len(i)
				time.sleep(0.05)
				#print 'After join, i equal :' + str(i)
			for i in xrange(128):
				try: # This is the wild scanner, must add the "neighborhourjeoitjreiotrje" one (damn word!)
					#print 'Start your engines'
					if listpublicip[0] >= 255:
						listpublicip[0] = random.choice(thirdgroup)
					elif listpublicip[1] > 255:
						listpublicip[1] = random.choice(thirdgroup)
					elif listpublicip[2] > 255:
						listpublicip[2] = random.choice(thirdgroup)
					myip = str(random.choice(firstgroup)) + '.' + str(listpublicip[1]) + '.' + str(listpublicip[2])
					myip = str(myip)
					#print myip
					threadhandler = threading.Thread(target=mythreadedscan.threadedscan, args=(myip, range1, range2, q, firsttime))
					listpublicip[2] = int(listpublicip[2]) + 1
					threads.append(mythreadedscan)
					threadhandler.start()
				except:
					print 'oops', sys.exc_info()
					print "J'ai merde"
					#pass
