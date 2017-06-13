a = input("Enter the array to be sorted : ")

def insertion(a):
	n = len(a)
	i = 1
	
	while i <= n-1:
		value = a[i]
		j = i-1
		while j>= 0 and a[j] > value:
			a[j+1] = a[j]
			j = j-1

		a[j+1] = value
		i = i+1
	print a,

insertion(a)
