#!/usr/bin/python
# coding=UTF-8
#What i do?:
#I'm a big lazy script who only launch trhead, collect user input and send it to my thread, then get it back
import socket, threading, os, sys, signal, sender, receiver, hashlib, pickle
from scanhandler import Scanthreader
from Queue import Queue
peers = {}
kbdata = ''
dst = ''
ASKMESSAGE = ''
dsthash = ''
emailhash = ''
class kbdinput():
	def keyboard_input(self, out_q):
		print 'Please enter your e-mail.'
		emailinput = raw_input()
		#print 'Displayer line 19 peers is : ' + str(Scanhandler.nodetable)
		emailhash = hashlib.md5(emailinput).hexdigest()
		print 'email hash is ' + emailhash
		out_q.put(emailhash)
		while 1: #This is where i get data
			msgqueue = threading.Thread(target=mykbdinput.message_queue, args=(q,))
			print 'email hash is ' + emailhash
			print 'Keyboard input time'
			kbdata = raw_input()
			try:
				peers = pickle.load( open("peers.txt", "rb" ) )
			except:
				print 'Error' , sys.exc_info()
			print type(kbdata)
			print 'Enter the destination (email)'
			dstmail = raw_input() #This method DOES NOT handle copy past with empty lines
			dsthash = hashlib.md5(dstmail).hexdigest()
			dst = peers.get(dsthash)
			print 'dst from displayer : ' + str(dst)
			print '1'
			# return kbdata
			# print '2'
			# return dst
			print '3'
			msgqueue.start()
			print '4'
			out_q.put(kbdata)
			out_q.put(dst)
			out_q.put(peers)
			out_q.put(ASKMESSAGE)
			out_q.put(dsthash)
			out_q.put(dstmail)
			#print 'Displayer line 19 peers is : ' + str(abcScanner.nodetable)
	#def message_queue(self, kbdata, dst, peers, ASKMESSAGE, dsthash):
	def message_queue(self, in_q ):
				print 'message_queue started'
				# Seems that those localvar copy is not doing what i want
				localvar = threading.local()
				localvar.kbdata = in_q.get()
				localvar.dst = in_q.get()
				localvar.peers = in_q.get()
				localvar.ASKMESSAGE = in_q.get()
				localvar.dsthash = in_q.get()
				localvar.x = 0
				localvar.dstmail = in_q.get()
				print 'localvar.kbdata :' + localvar.kbdata
				print 'localvar.dst :' + str(localvar.dst)
				print 'localvar.peers :' + str(localvar.peers)
				print 'localvar.ASKMESSAGE :' + localvar.ASKMESSAGE
				print 'localvar.dsthash :' + localvar.dsthash
				if localvar.kbdata:
					while localvar.dst is None:
						print 'User unknown'
						for key in localvar.peers.iterkeys():
							print 'key' + str(key)
							localvar.dst = localvar.peers.get(key)
						#while localvar.x == len(localvar.peers): #This is almost pseudo code..
							localvar.ASKMESSAGE = 'WHEREIS' + ',' + localvar.dsthash #Step one : Ask others known nodes
							myhand.sendmessage(emailhash, localvar.dst, localvar.ASKMESSAGE)
							localvar.x = localvar.x + 1
						try:					
							with open("peers.txt", "rb") as picklefile:
								localvar.peers = pickle.load(picklefile) #Step two, reload the peers "DB" and try again, the scanner may had find the wanted node by himself
							localvar.dsthash = hashlib.md5(localvar.dstmail).hexdigest()
							localvar.dst = localvar.peers.get(dsthash)
						except:
							print 'Still file not found ?!', sys.exc_info()
							pass
						break
				elif dst is not None:
						myhand.askfornode(emailhash, localvar.dst, localvar.kbdata) #i use the function in sender.py to send data
				else:
						pass
				# except:
					# print 'Error', sys.exc_info() #Nope sir... TODO:handle ctrl+c for quit or add a keyword for quitting
					# break
q = Queue()
mygest = receiver.Gest()
myhand = sender.Messagehandling()
myscanner = Scanthreader()
mykbdinput = kbdinput() #Threading section, do NOT make infinite loop of this, as thread already loop themselves.
conhandler = threading.Thread(target=mygest.handler, args=(q,))
kbdhandler = threading.Thread(target=mykbdinput.keyboard_input, args=(q,))
scanhandler = threading.Thread(target=myscanner.threader,)
#msgqueue = threading.Thread(target=mykbdinput.message_queue, args=(kbdata, dst, peers, ASKMESSAGE, dsthash,))
conhandler.start()
kbdhandler.start()
scanhandler.start()
#msgqueue.start(kbdata, dst, peers, ASKMESSAGE, dsthash,)



