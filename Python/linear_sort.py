a = input("Enter an array : ")

n = len(a)

i = 0
while i < n:
	j = i+1
	while j < n:
		if a[i] > a[j]:
			temp = a[i]
			a[i] = a[j]
			a[j] = temp
		j = j+1

	i = i + 1
print a, 