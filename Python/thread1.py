from threading import Thread
from time import sleep
from threading import Lock

class my_thread(Thread):

	def __init__(self,name,msg):
		Thread.__init__(self)
		self.name = name
		self.msg = msg

	def run(self):
		l.acquire()
		i = 0
		while i<len(self.msg):
			k = open("thread.txt",'a')
			k.write(self.msg[i])
			print self.msg[i]
			i = i+1
			sleep(1)
			k.close()
		l.release()		

l = Lock()

t1 = my_thread('thread_1','Valar Morghulis')
t1.start()	#main thread runs internally which is the benifit of using threading module but only one thread runs. Use t1.start()
#t1.join()

t2 = my_thread('thread_2','A lannister always pays his debts')
t2.start()
#t2.join()
