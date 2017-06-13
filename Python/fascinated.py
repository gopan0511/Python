def check_fascinated(no):
	flag = 0
	s = str(no*1) + str(no*2) + str(no*3)
	print s, type(s)

	if len(s) == 9:
		if '0' not in s:
			i = 0
			while i < len(s):
				j=i+1
				while j<len(s):
					if s[i]==s[j]:
						print 'not fascinated'
						flag = 1
					j+=1
				i+=1
				if flag == 1:
					break
			else:
				print 'Yes it is a fascinated number'
				
		else:
			print 'not fascinated'	
		
	else:
		print 'not fascinated'




def main():
	no = input("Enter a number : ")
	check_fascinated(no)
	
main()

