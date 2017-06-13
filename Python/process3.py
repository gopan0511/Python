#To kill a child inside the parent process

from time import sleep
from os import fork,kill,getpid,wait
from signal import signal

def bbsr(x,y):
	print '%x'%id(bbsr)
	print x,y
	print 'Parent knows child is dead'

def ctc(x,y):
	print 'I got SIGINT signal'
	exit(0)

signal(17,bbsr)
signal(2,ctc)

k = fork()

i = 0
if k == 0:

	while 1:	#child
		#if i == 5:
		#	kill(getpid(), 3)
		#i+=1
		print 'I am a child'
		sleep(1)

else:	#parent
	while 1:
		if i == 5:
			kill(k,3)
			pid,status = wait()
		i+=1
		print 'I am parent'
		sleep(1)
	
