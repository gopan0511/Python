def factorial(n):
	result = 1
	for c in range(1,n+1):
		result = result *c

	return result

def main():
	n = input("Enter the number of rows : ")

	for i in range(0,n):
		for c in range(0,(n-i-1)):
			print "",

		for c in range(0,i+1):
			print factorial(i)/((factorial(c))*factorial(i-c)),

		print "\n"

main()