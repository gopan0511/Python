from os import wait,kill,getpid,fork
from time import sleep
from signal import signal,SIG_IGN

def bbsr(x,y):
	print '%d'%id(bbsr)
	print x,y
	print 'Parent knows child is dead'

def ctc(x,y):
	print 'I got SIGINT signal'
	exit(0)

k = fork()

if k == 0:	#child
	i = 0
	while 1:
		print 'I am  a child process'
		sleep(1)

else:	#parent
	i = 0
	while 1:
		if i == 10:
			kill(k,3) #child becomes defunct/zombie process
		if i == 20:
			pid,status = wait()
		i+=1
		print "I am a parent process"
		sleep(1) 
	
