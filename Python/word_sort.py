def main():
	s = raw_input("Enter a string : ")

	l = s.split()
	print l

	n = len(l)
	i = 1	
	while i <= n-1:
		value = l[i]
		j = i-1
		while j>= 0 and l[j] > value:
			l[j+1] = l[j]
			j = j-1

		l[j+1] = value
		i = i+1
	print l

	for words in l:
		print words
main()