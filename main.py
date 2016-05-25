#!/usr/bin/python
import socket, thread, os, sys, signal
Host = '0.0.0.0'
Port = 4242
BUFF = 32
def response(key):
    return 'OK!' + key
class Gest():
    # def __init__(self):
        # pass #why does that init forbid the method handler to be registered?
	def handler(self, clientsock, addr):
		receivedlendata = 0
		fromclientlendata = 0
		lenreceived = False
		clientsock.settimeout(140) 
		while 1:
			try:
				print 'while 1'
				#if not data: break
				#data = str(data)
				# OBELIXcurrentdatasize = 0
				# if data == 'OBELIX':
					# fromclientlendata = data[1]
					# while OBELIXcurrentdatasize < fromclientlendata:
						# print 'Obeliiiix!'
						# data = clientsock.recv(BUFF)
						# if len(data) + OBELIXcurrentdatasize > receivedlendata:
							# data = data[:receivedlendata - OBELIXcurrentdatasize]
				# else:
				#print data
				if lenreceived is not True:
					data = clientsock.recv(BUFF)
					data = data.split(',', 1)
					receivedlendata = data[0]
					receivedlendata = int(receivedlendata)
					lenreceived = True
					print len(data)
					print data
				if receivedlendata > BUFF:
					print 'Obeliiiix!'
					print receivedlendata
					print len(data)
					count = 0
					while len(data) < receivedlendata:
						print count
						print 'while 2'
						#packet = clientsock.recv(r/
						.
						3.20/eceivedlendata - len(data))
						packet = clientsock.recv(BUFF)
						if not packet:
							return None
						data += packet
						print len(data)
						print len(packet)
						data = str(data)
					return data
				else:
					fromclientlendata = len(data[1])
					print 'Asteeriiixx!'
					print data
					print type(data)
					print type(fromclientlendata)
					print type(receivedlendata)
				if receivedlendata == fromclientlendata:
					print 'datasizecompare done OK '
					clientsock.send('OK!')
				else:
					print 'datasizecompare done NOK'
					clientsock.send('NOK')
			except:
				clientsock.send('Erreur, message incorrect')
				print 'Error', sys.exc_info()
				
mygest = Gest()				
if __name__ == '__main__':
    ADDR = (Host, Port)
    serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serversock.bind(ADDR)
    serversock.listen(5)
    #mychecklogin = Checklogin()
    while 1:
        try:
            print 'waiting for connection... listening on port', Port
            clientsock, addr = serversock.accept()
            print '...connected from:', addr
            thread.start_new_thread(mygest.handler, (clientsock, addr))
        except KeyboardInterrupt:
            print "\nCraaac"
            os.remove('server.pid')
            serversock.shutdown
            serversock.close
            os._exit(0)