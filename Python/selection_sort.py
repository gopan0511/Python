a = input("Enter the array : ")

i = 0
while i < len(a):
	s = i
	j = i+1
	while j < len(a):
		if a[s] > a[j]:
			s = j
		j = j+1
	temp = a[i]
	a[i] = a[s]
	a[s] = temp
	i = i+1
print a