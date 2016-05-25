#!/usr/bin/python
import socket, thread, os, sys, signal, time
i = 0
class Mptest1:
	def mptest1(self, ):
		i = 0
		#while i < 10:
		print "\nI'm Process 1"
		time.sleep(1)
		i = i + 1
class Mptest2:
	def mptest2(self, ):
		i = 0
		#while i < 10:
		print "\nI'm Process 2"
		time.sleep(2)
		i = i + 1
class kbdinput():
	def keyboard_input(self,):
		while 1:
			try:
				#thread.get_ident()
				#print kbdata
				#print 'Keyboard input time\n',
				#print gotmail
				kbdata = raw_input()
				print type(kbdata)
				# print 'Enter the destination (IPv4)'
				# dst = raw_input()
				#string = kbdata
				#myhand.sendmessage(kbdata, dst)
				print kbdata
				#myhand.getmessage(data)
				#myhand.getmessage()
				#print data
					#print myhand.getmessage()
				#break
				kbdata = ''
			except:
				print 'Error', sys.exc_info()#[0]
				break
			print 'test'
mykbdinput = kbdinput()
mymptest1 = Mptest1()
mymptest2 = Mptest2()
while True:
	thread.start_new_thread(mymptest1.mptest1, ())
	time.sleep(1)
	thread.start_new_thread(mymptest2.mptest2, ())
	time.sleep(2)
thread.start_new_thread(mykbdinput.keyboard_input, ())