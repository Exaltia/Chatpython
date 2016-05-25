#!/usr/bin/python
# coding=UTF-8
import socket, thread, os, sys, signal, client2, main2
#from client2 import *
#from main2nonthreaded import *
print TCP_IP
myhand = Messagehandling()
mygest = Gest()
#print dir (myhand)
#data = ''
#BUFF = 1024
# def Client(string):
    # HOST, PORT = '127.0.0.1', 4242
    #SOCK_STREAM == a TCP socket
    # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # sock.setblocking(0)  # optional non-blocking
    # sock.connect((HOST, PORT))
    # sock.send(string)
    # reply = sock.recv(1024)  # limit reply to 16K
    #sock.close()
    # return reply
# myclient = Client('prout')
class kbdinput():
	def keyboard_input(self,):
		while 1:
			try:
				print 'Keyboard input time'
				#print gotmail
				kbdata = raw_input()
				print type(kbdata)
				print 'Enter the destination (IPv4)'
				dst = raw_input()
				#string = kbdata
				myhand.sendmessage(kbdata, dst)
				print data
				#myhand.getmessage(data)
				#myhand.getmessage()
				#print data
					#print myhand.getmessage()
				#break
			except:
				print 'Error', sys.exc_info()#[0]
				break
			print 'test'
mykbdinput = kbdinput()
	#print result
# class Client():
	# def handler(self, clientsock, addr):
		# clientsock.settimeout(140)

		# while 1:
			# try:
				# data = clientsock.send(BUFF)
				# if not data: 
					# breaki
			# except:s
				# print 'floodhumhum'
# if __name__ == '__main__':
	# try:
# myclient = Client()
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# thread.start_new_thread(myclient.handler, ('127.0.0.1', 4242))
# print 'socket opened'

	# except:
		# print 'No connexion, try again'



