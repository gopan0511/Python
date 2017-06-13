from os import kill,getpid,fork
from time import sleep
from sys import argv
from signal import signal

def bbsr(x,y):
	print "I am SIGQUIT signal"
	exit(0)

signal(3,bbsr) #this is the signal handler which handles the signal and calls the bbsr() when the child is killed.

if len(argv) == 2:
	print "okay"

	k = fork()

	if k == 0:	#child
		if argv[1] == 'start':
			fo = open("lit.txt",'a')
			fo.write(str(getpid()))
			fo.close()
			while 1:
				print "I am child"
				sleep(1)

	else:	#parent
		if argv[1] == 'stop':
			print "Parent is killing child"
			fo = open("lit.txt",'r')
			pidlist = fo.readlines()
			if len(pidlist) == 0:
				print "failed since the file is empty!!"
				exit(0)
			fo.close()
			
			for pid in pidlist:
				kill(int(pid),3)
			fo = open("lit.txt",'a')
			fo.write(' ')
			fo.close()
						

else:
	print "Not okay"
