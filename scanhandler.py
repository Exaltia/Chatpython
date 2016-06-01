#!/usr/bin/python
import threadedscan, threading, socket, sys, time, random, os
from requests import get
from Queue import Queue
q = Queue()
processq = Queue(maxsize=128)
num_threads = 128
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
range2 = 254
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
for num in range (1, 127):
	firstgroup.append(num)
for num in range (128, 256):
	secondgroup.append(num)
for num in range (1, 256):
	thirdgroup.append(num)
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
	for i in range(128):
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
			mysupertest = threading.Thread(target=mytest.testtest, args=(myip, range1, range2, q, firsttime))
			mysupertest.daemon = True
			listpublicip[2] = int(listpublicip[2]) + 1
			#print i
			threads.append(mysupertest)
			mysupertest.start()
		except:
			#print 'oops', sys.exc_info()
			pass
	#print 'Je join'
	mysupertest.join
	time.sleep(1.65)
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
	runs = runs + 1
	# if runs == 2:
		# print 'CRAC!'
	if a:
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