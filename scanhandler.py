#!/usr/bin/python
#This file is (soon!) to be launched by displayer and handle the scan threads
import threadedscan, threading, sys, time, random, os
from requests import get
from Queue import Queue
from pympler import muppy, summary #Memory leak tracker, remove once debugued
from pympler import refbrowser
def output_function(o):
	return str(type(o))
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
mytest = threadedscan.Testeur()
myip = listpublicip[0] + '.' + listpublicip[1] + '.' + listpublicip[2] + '.'
myip = str(myip)
range1 = 1
range2 = 2
b = []
firstgroup = []
secondgroup = []
thirdgroup = []	
fourthgroup = []
sleeptime = 0
a = {}
runs = 0
firsttime = 0
#i = 0
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
while len(a) < 21:
	#print 'len true'
	#while int(listpublicip[2]) < 255:
	#while runs < 128:
		#print 'while TRUE!'
		#print 'runs is :' + str(runs)
	#print myip
	#sleeptime = sleeptime + 0.1 * 2
	#print myip
		#print i
	all_objects = muppy.get_objects()
	for i in xrange(1):
		try:
			#print 'Start your engines'
			if listpublicip[0] > 255:
				listpublicip[0] = random.choice(thirdgroup)
			elif listpublicip[1] > 255:
				listpublicip[1] = random.choice(thirdgroup)
			elif listpublicip[2] > 255:
				listpublicip[2] = random.choice(thirdgroup)
			myip = str(random.choice(firstgroup)) + '.' + str(listpublicip[1]) + '.' + str(listpublicip[2])
			myip = str(myip)
			#print myip
			mysupertest = threading.Thread(target=mytest.testtest, args=(myip, range1, range2, q, firsttime))
			#mysupertest.daemon = True
			listpublicip[2] = int(listpublicip[2]) + 1
			#print i
			#print 'Je vais append'
			threads.append(mysupertest)
			#print len(threads)
			#print "j'ai append"
			#print 'Threads type is :' + type(threads)
			mysupertest.start()
			#threads.start(mysupertest)
			#print "j'ai start"
		except:
			print 'oops', sys.exc_info()
			#print "J'ai merde"
			pass
	#print 'Je join'
	threads = []
	mysupertest.join
	#time.sleep(10)
	sum1 = summary.summarize(all_objects)
	summary.print_(sum1)
			# if i == 128:
				# mysupertest.join
				# print 'Do a barrel roll'
				# time.sleep(3)
				#break
		# except thread.error:
			# print 'Error', sys.exc_info()
			# time.sleep(30)
			# pass
	#threads.append(mysupertest)
	#print runs
	a = q.get()
	#runs = runs + 1
	# if runs == 2:
		# print 'CRAC!'
	if a:
		print 'HAN! A pas vide!'
		print a
	# elif len(a) < 21 and runs == 128:
		# print 'Nothing found, trying again'
		# mysupertest.join()
		# listpublicip[2] = 0
		# runs = 0
		#time.sleep(10)
		#mysupertest.join()

print 'hop'
print 'byebye'