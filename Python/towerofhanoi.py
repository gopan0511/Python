count = 0

n = input("Enter the number of discs to be transfered : ")

def towerOfHanoi(n,source,temp,dest):
	global count
	
	if n == 1:
		print "Move disc 1 from %c to %c"%(source,dest)
		count = count + 1
		return
	
	towerOfHanoi(n-1,source,dest,temp)
	
	print "Move disc %d from %c to %c"%(n,source,dest)
	
	count = count + 1
	towerOfHanoi(n-1,temp,source,dest)

towerOfHanoi(n,'A','B','C')

print "The number of moves required = ",count

