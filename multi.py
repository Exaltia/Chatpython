#!/usr/bin/python
import multiprocessing
import mptest1
import mptest2
import time, sys
if __name__ == '__main__':
	multiprocessing.set_start_method('fork')
	#while True:
	p1 = Process(target=mptest1())
	p2 = Process(target=mptest2())
	#p1.set_start_method('fork')
	#p2.set_start_method('fork')
	#p1.daemon = True
	p2.daemon = True
	p1.daemon = True
	p1.start
	print dir(multiprocessing)
	p2.start()
	# p1.join()
	# p2.join()
	#print "I'm the multi forker"
	#time.sleep (8)