n = input("Enter a number : ")

def fact(n):
	if n == 0 or n==1:
		return 1
	if n>1:
		return n*fact(n-1);
f = fact(n)
print f