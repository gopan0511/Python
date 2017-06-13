from os import fork,wait
from time import sleep

k = fork()

if k == 0:
	cmsg = "I am Child Process";
	ind = 0;
	while ind < len(cmsg):
		fo = open("lit.txt",'a')
		fo.write(cmsg[ind])
		print cmsg[ind]
		ind +=1
		sleep(1)
		fo.close()
	exit(0)

else:
	pid,status = wait()
	print pid,status
	sleep(10)
	pmsg = "I am Parent Process"
	ind = 0
	while ind < len(pmsg):
		fo = open("lit.txt",'a')
		fo.write(pmsg[ind])
		print pmsg[ind]
		ind +=1
		sleep(1)
		fo.close()

