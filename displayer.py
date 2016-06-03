#!/usr/bin/python
# coding=UTF-8
#What i do?:
#I'm a big lazy script who only launch trhead, collect user input and send it to my thread, then get it back
import socket, threading, os, sys, signal, sender, receiver, hashlib, scanhandler
from Queue import Queue
mygest = receiver.Gest()
myhand = sender.Messagehandling()
class kbdinput():
	def keyboard_input(self, out_q):
		peers = {}
		print 'Please enter your e-mail.'
		try:
			with open("peers.txt", "r") as mypeers:
				eval(peers) = mypeers.readlines()
		except:
			pass
		emailinput = raw_input()
		emailhash = hashlib.md5(emailinput).hexdigest()
		print 'email hash is ' + emailhash
		out_q.put(emailhash)
		while 1: #This is where i get data
			try:
				print 'email hash is ' + emailhash
				print 'Keyboard input time'
				kbdata = raw_input()
				print type(kbdata)
				print 'Enter the destination (email)'
				dstmail = raw_input() #This method DOES NOT handle copy past with empty lines
				dsthash = hashlib.md5(dstmail).hexdigest()
				dst = peers.get(dsthash)
				if dst == None:
					print 'User unknown'
					break
				else:
					myhand.sendmessage(kbdata, dst) #i use the function in sender.py to send data
			except:
				print 'Error', sys.exc_info() #Nope sir... TODO:handle ctrl+c for quit or add a keyword for quitting
				break
q = Queue()
myscanner = scanhandler.Scanthreader()
mykbdinput = kbdinput() #Threading section, do NOT make infinite loop of this, as thread already loop themselves.
conhandler = threading.Thread(target=mygest.handler, args=(q,))
kbdhandler = threading.Thread(target=mykbdinput.keyboard_input, args=(q,))
scanhandler = threading.Thread(target=myscanner.threader,)
conhandler.start()
kbdhandler.start()
scanhandler.start()




