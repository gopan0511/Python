
num = input("Enter a number : ")

factorial = 1

if num < 0:
	print "It is not possible to find the factorial of negative numbers!!"

elif num == 0:
	factorial = 1

else:
	for i in range(1,num+1):
		factorial = factorial*i

print "Factorial of the number is %d"%factorial