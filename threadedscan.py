#!/usr/bin/python
#Scan, scan, scan, and more scan, I WANT FRIENDS!
from Queue import Queue
import time, socket, sys, time, random, os, datetime #Datetime is for debug purpose only on the already in progress error diag
class Scanner():
	def threadedscan(self, myip, range1, range2, out_q, firsttime,):
		PORT = 4242
		BUFF = 1000
		MESSAGE = 'WHOAREU'
		message = ''
		# firstgroup = []
		# secondgroup = []
		# thirdgroup = []
		# fourthgroup = []
		bb = []
		nodetable = {}
		for num in range(range1, range2):
			host = myip + '.' + str(num)
			#host = '212.83.136.107' # for debug, testing quickly my own node (who is at .137)
			#ADDR = (host, self.PORT)
			#print host
			try:
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				s.settimeout(0.65)
				
				#s.setblocking(1)
				
				s.connect((host, PORT))
				
				lenmsg = len(MESSAGE)
				lenmsg = str(lenmsg)
				print 'lenmsg is :' + len(lenmsg)
				protomsg = lenmsg + ','+ '' + ',' + MESSAGE #client Wait for the following message : "messagelenght,message"
				s.send(protomsg)
				#print 'i send'
				packet = s.recv(BUFF)
				#print len(packet)
				if 'MIAOU' in packet: #Check if it's one of our node by sending miaou
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
				s.close
				#print 'host' + host +  'except' + str(datetime.datetime.now()), sys.exc_info()
				#print 'je vais close'
				#s.close
				#s.shutdown(socket.SHUT_RDWR)
				#print len(nodetable)
					#time.sleep(0.1)
					#print bb
				#print 'Pouet'
			#print 'Going to out_q'
			out_q.put(nodetable)
			#print host
			# print 'i close' + host + str(datetime.datetime.now())
			
			# print host + 'Closed' + str(datetime.datetime.now())
			# del host
			# del lenmsg
			# del MESSAGE
			# del protomsg
			# del bb
			# del nodetable
		#print 'fini'
		#s.shutdown()
		#sys.exit(0)
		#return(nodetable)
q = Queue()

