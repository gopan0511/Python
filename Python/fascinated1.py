no = input("Enter a number : ")

s = str(no*1) + str(no*2) + str(no*3)

print s

l = list(s)
l.sort()

print l
if l == ['1','2','3','4','5','6','7','8','9']:
	print "fascinated number"
else:
	print 'not a fascinated number'
