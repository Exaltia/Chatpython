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
	def handler(self,):
		while True: # Message reception infinite loop
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
				data += packet
				amount_received = data.split(',', 1)
				amount_received = len(amount_received[1])
				amount_expected = data.split(',', 1)
				amount_expected = int(amount_expected[0])
			print 'while ended'
			final = data.split(',', 1)
			final = final[1]
			if len(final) == amount_expected:
				final2 = 'Ok!'
				gotmail = 'Message recu de ' + str(addr) + 'contenant :' + final
				print gotmail
				clientsock.send(gotmail)
				print 'Ok'
			print 'waiting for connection... listening on port', Port
mygest = Gest() # Hum... errr... is this line still usefull? must test		
ADDR = (Host, Port) #Server socket creation
serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversock.bind(ADDR)
serversock.listen(5)	
