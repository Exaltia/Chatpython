#!/usr/bin/python
import socket, sys
PORT = 4242
point = '.'
BUFF = 1000
MESSAGE = 'WHOAREU'
for num in range(1,254):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(0.05)
	host = '192.168.0.' + str(num)
	#print '\r In progress' + point
	#print host + str(PORT)
	ADDR = (host, PORT)
	try:
		s.connect((host, PORT))
		lenmsg = len(MESSAGE)
		lenmsg = str(lenmsg)
		protomsg = lenmsg + ','+ '' + ','+ MESSAGE #client Wait for the following message : "messagelenght,message"
		s.send(protomsg)
		packet = s.recv(BUFF)
		if packet:
			print 'Found node ' + packet + ' at ' + str(host)
			s.close()
		#point = point + '.'
	except:
		#print 'E', sys.exc_info()
		s.close()
print 'Finished'
