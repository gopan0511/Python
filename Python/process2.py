from multiprocessing import Process
from time import sleep

def bbsr(name,stime,ctime):
	for i in range(ctime):
		print("I am",name)
		sleep(stime)

p1 = Process(target = bbsr,args = ('child_1',1,5))
p1.start()
p1.join()

p2 = Process(target = bbsr,args = ('child_2',2,10))
p2.start()
p2.join()

while 1:
	print('I am parent')
	sleep(1)
