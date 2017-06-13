a = input("Enter an array : ")

n = len(a)

i = 0
while i < n:
	j = 0
	while j < n-i-1:
		print j,(j+1)
		j = j+1

	i = i + 1
 