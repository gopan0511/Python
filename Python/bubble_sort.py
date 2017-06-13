a = input("Enter the array to be sorted : ")


def bubble(a):
	n = len(a)
	i = 0
	while i < n-1:
		j = 0
		while j < n-i-1:
			if a[j] > a[j+1]:
				temp = a[j]
				a[j] = a[j+1]
				a[j+1] = temp
			j += 1
		i += 1
	print a,

bubble(a)