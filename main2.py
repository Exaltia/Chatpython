#!/usr/bin/python
import socket, threading, os, sys, signal, time, client2
Host = '0.0.0.0'
Port = 4242
BUFF = 16384
from __main__ import *
def response(key):
    return 'OK!' + key
class Gest():
	def kbdinput(self,):
		print 'all your base belong to tab'
		while 1:
			try:
				#print gotmail
				kbdata = raw_input()
				print type(kbdata)
				print 'Enter the destination (IPv4)'
				dst = raw_input()
				myhand.sendmessage(kbdata, dst)
				print data
				myhand.getmessage(data)
				myhand.getmessage()
				print data
				print myhand.getmessage()
				break
			except:
				print 'Error', sys.exc_info()#[0]
				break
			print 'test'
    # def __init__(self):
        # pass #why does that init forbid the method handler to be registered?
	#def handler(self, clientsock, addr):
	def handler(self,):
		while True:
			print 'Started'
			receivedlendata = 0
			fromclientlendata = 0
			lenreceived = False
			print 'stuck?'
			clientsock, addr = serversock.accept()
			print 'not stuck, no nono no'
			clientsock.settimeout(140)
			data = ''
			packet = ''
			lendata = ''
			print 'Je reviens avant le while'
			amount_received = 0
			amount_expected = 99999999999999999999999999999999999
			while amount_received < amount_expected:
				packet = clientsock.recv(BUFF)
				data += packet
				#print data
				amount_received = data.split(',', 1)
				amount_received = len(amount_received[1])
				amount_expected = data.split(',', 1)
				#print amount_expected
				amount_expected = int(amount_expected[0])
				#print 'amount expected is :' + str(amount_expected)
			print 'while ended'
			final = data.split(',', 1)
			final = final[1]
			#print len(data)
			if len(final) == amount_expected:
				final2 = 'Ok!'
				#clientsock.send(final2)
				gotmail = 'Message recu de ' + str(addr) + 'contenant :' + final
				print gotmail
				clientsock.send(gotmail)
				#clientsock.send(data)
				print 'Ok'
				# data = ''
				# packet = ''s
				# amount_received = 0
				# amount_expected = 99999999999999999999999999999999999
			print 'waiting for connection... listening on port', Port
mygest = Gest()		
print dir(mygest)		
#if __name__ == '__main__':
ADDR = (Host, Port)
serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversock.bind(ADDR)
serversock.listen(5)
#serversock.setblocking(0)
    #mychecklogin = Checklogin()
conhandler = threading.Thread(target=mygest.handler,)
kbdhandler = threading.Thread(target=mygest.kbdinput,)
conhandler.start()
kbdhandler.start()
# while 1:
	# try:
		# clientsock, addr = serversock.accept()
		# print '...connected from:', mygest.handler(addr)
		# thread.start_new_thread(mygest.handler, (clientsock, addr))
		# conhandler = threading.Thread(target=mygest.handler,)
		# conhandler.start()
		# thread.start_new_thread(mygest.handler, ())
		# time.sleep(5)
	# except KeyboardInterrupt:
		# print "\nCraaac"
		# os.remove('server.pid')
		# serversock.shutdown
		# print 'shutdown done'
		# serversock.close
		# print 'close done'
		# os._exit(0)
print 'youhou'

#thread.start_new_thread(mygest.kbdinput, ())
#time.sleep(60)
#while 1:
