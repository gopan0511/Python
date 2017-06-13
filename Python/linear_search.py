n = input("Enter an array : ")

key = input("Enter the key element to be found ")

def linear(n,key):
	i = 0
	for i in range(len(n)):
		if key ==  n[i]:
			print "Element is found"
			break
		i += 1	
	else:
		print "Element is not found"
		
linear(n,key)