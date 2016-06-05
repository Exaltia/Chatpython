#!/usr/bin/python
# coding=UTF-8
#What i do?:
#i'm launcher as a thread by displayer and my favorite activity is to get data typed from the user in displayer then send it and pass it back at displayer	
import socket, time, receiver
#TCP_IP = '127.0.0.1' # If it doesn't work anymore remove comment
Port = 4242 # Maybe : Move this hardcoded values to a setting file
BUFF = 16384 # Do NOT move that to a setting file, or be sure that pebcak while occur
amount_sent = 0
announce = ''
MESSAGE = ''
ASKMESSAGE = ''
result = ''
sentannounce = False
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
class Messagehandling():
	def sendmessage(self, dsthash , TCP_IP, MESSAGE):
		print 'Sending'
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((TCP_IP, Port))
		lenmsg = len(MESSAGE)
		lenmsg = str(lenmsg)
		protomsg = lenmsg + ',' + dsthash + ',' + MESSAGE #client Wait for the following message : "messagelenght,message"
		print len(protomsg) #Debug line, could be removed Soon(tm)
		s.send(protomsg) # send message to the specified client
		print 'sent'
		data = s.recv(BUFF) #Cause the sent message to be immediatly displayed on the sender screen, will be used to construct the chatlog, finally maybe using that to check that the sender got the message would be better
		s.close()
		print "received data:", data #Debug line, could be removed Soon(tm)
	def askfornode(self, dsthash , TCP_IP, ASKMESSAGE): # Used when the node is unknown
		print 'Asking for nodes'
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((TCP_IP, Port))
		lenmsg = len(ASKMESSAGE)
		lenmsg = str(lenmsg)
		protomsg = lenmsg + ',' + dsthash + ',' + ASKMESSAGE #client Wait for the following message : "messagelenght,message"
		print 'TCP_IP' + TCP_IP
		print 'dsthash' + dsthash
		print 'lenmsg' + lenmsg
		print 'ASKMESSAGE' + ASKMESSAGE
		s.send(protomsg)
		s.close()
		