n = input("Enter a number : ")
def Function(n):
	count = 0
	for i in range(n/2,n):
		j = 1
		while j + n/2 <= n:
			k = 1
			while k <= n:
				count = count + 1
				k = k * 2
			j = j + 1
	print count,

Function(n)