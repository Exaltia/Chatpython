#!/usr/bin/python
from Queue import Queue
import time, socket, sys, time, random, os
class Testeur():
	def testtest(self, myip, range1, range2, out_q, firsttime,):
		PORT = 4242
		BUFF = 1000
		MESSAGE = 'WHOAREU'
		message = ''
		firstgroup = []
		secondgroup = []
		thirdgroup = []
		fourthgroup = []
		bb = []
		nodetable = {}
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(0.65)
		for num in range (range1, range2):
			host = myip + '.' + str(num)
			#print host
			#ADDR = (host, self.PORT)
			try:
				#print 'je try'
				#s.setblocking(0)
				#print 'socket setted up'
				s.connect((host, PORT))
				#print 'I connect'
				lenmsg = len(MESSAGE)
				lenmsg = str(lenmsg)
				protomsg = lenmsg + ','+ '' + ',' + MESSAGE #client Wait for the following message : "messagelenght,message"
				s.send(protomsg)
				#print 'i send'
				packet = s.recv(BUFF)
				if 'MIAOU' in packet:
					#print 'Found node ' + packet + ' at ' + str(host)
					packet = packet.split(',' ,1)
					packet = str(packet[1])
					nodetable = {packet, host}
					print host
					#if nodetable:
						#print nodetable
					#print nodetable
				#time.sleep(0.5)
				#print 'je vais close'
				s.close()
			except:
				#print 'host' + host +  'except', sys.exc_info()
				#print 'je vais close aussi'
				s.close()
				time.sleep(0.05)
					#time.sleep(0.1)
					#print bb
				#print 'Pouet'
			#print 'Going to out_q'
			out_q.put(nodetable)
q = Queue()