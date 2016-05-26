#!/usr/bin/python
# coding=UTF-8
#What i do?:
#I'm a big lazy script who only launch trhead, collect user input and send it to my thread, then get it back
import socket, threading, os, sys, signal, sender, receiver
mygest = receiver.Gest()
myhand = sender.Messagehandling()
class kbdinput():
	def keyboard_input(self,):
		while 1: #This is where i get data
			try:
				print 'Keyboard input time'
				kbdata = raw_input()
				print type(kbdata)
				print 'Enter the destination (IPv4)'
				dst = raw_input() #This method DOES NOT handle copy past with empty lines
				#string = kbdata
				#print dir(myhand)
				#myhand.sendmessage(kbdata, dst)
				myhand.sendmessage(kbdata, dst) #i use the function in sender.py to send data
				#print data
				#myhand.getmessage(data)
				#myhand.getmessage()
				#print data
					#print myhand.getmessage()
				#break
			except:
				print 'Error', sys.exc_info() #Nope sir... TODO:handle ctrl+c for quit or add a keyword for quitting
				break
			print 'test'
mykbdinput = kbdinput() #Threading section, do NOT make infinite loop of this, as thread already loop themselves.
conhandler = threading.Thread(target=mygest.handler,)
kbdhandler = threading.Thread(target=mykbdinput.keyboard_input,)
conhandler.start()
kbdhandler.start()




