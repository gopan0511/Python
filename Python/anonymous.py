#To define an anonymous function we use lambda
''' Lambda function doesnot take any statement.
	It returns an expression
	It doesnot support variable length arguement
	'''
a = input("Enter a number : ")
b = input("Enter a number : ")


sum = lambda a,b : a + b
print sum(a,b)