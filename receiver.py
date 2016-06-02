#!/usr/bin/python
#What i do ?:
#I'm the server who is launched by displayer and return received data to this script
import socket, threading, os, sys, signal, time #,client2
Host = '0.0.0.0'

Port = 4242 # Maybe : Move this hardcoded values to a setting file
BUFF = 16384 # Do NOT move that to a setting file, or be sure that pebcak while occur
from __main__ import *
def response(key):
    return 'OK!' + key
class Gest():
	def handler(self, in_q):
		emailhash = in_q.get()
		miaouemailhash = 'MIAOU,' + emailhash
		while True: # Message reception infinite loop
			print 'emailhash: ' + str(emailhash)
			receivedlendata = 0
			fromclientlendata = 0
			lenreceived = False
			clientsock, addr = serversock.accept()
			clientsock.settimeout(140)
			data = ''
			packet = ''
			lendata = ''
			amount_received = 0
			amount_expected = 99999999999999999999999999999999999 #Dirty workaround to handle the very first time we check the following while. 
			#Will mess if user send more than 1,24TB of data in a single message XD.
			#Todo : Set up a maximum message lenght to avoid killing every computers
			#Todo : handle file sharing by adding a special loop for that
			#Todo : Use github tools to stop adding todo in code
			while amount_received < amount_expected:
				packet = clientsock.recv(BUFF)
				try:
					data += packet
					amount_received = data.split(',', 1)
					amount_received = len(amount_received[1])
					amount_expected = data.split(',', 1)
					amount_expected = int(amount_expected[0])
				except:
					print 'Protocole sur chaise roulante!'
			print 'while ended'
			try:
				final = data.split(',', 2)
				msg = final[2]
				userid = final[1]
				if len(msg) == amount_expected:
					if msg != 'WHOAREU':
						print msg
						gotmail = 'Message recu de ' + userid + 'contenant :' + msg
						print gotmail
						clientsock.send(gotmail)
						final2 = 'Ok!'
						msg = ''
					elif msg == 'WHOAREU':
						clientsock.send(miaouemailhash)
						msg = ''
						#clientsock.close()
			except:
				print 'Protocole fracture!', sys.exc_info()
try:
	with open("peers.txt", "r") as mypeers:
		peers = mypeers.readlines()
		print peers
except IOError:
	open('peers.txt, 'a').close()
	pass
mygest = Gest() # Hum... errr... is this line still usefull? must test		
ADDR = (Host, Port) #Server socket creation
serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversock.bind(ADDR)
serversock.listen(5)	
