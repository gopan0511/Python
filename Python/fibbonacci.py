r = input("Enter the range till you want the fibonacci series")

a,b = 0,1
print a,
for i in range(1,r):
	a,b = b,a+b
	print a,