a = [9,1,5,8,12,13,17]
b = [23,4,3,8]

for i in range(len(b)):
	a.append(b[i])


b =  sorted(a)
print b[0:7]
print b[7:]