#Output = [6,1,5,2,4,3]

a = [1,2,3,4,5,6]
b = len(a)

if b%2 == 0:
	mid = b/2
else:
	mid = b/2 + 1

c = []
for i in range(mid):
	c.append(a[b] - 1)
	c.append(a[i])
	b = b-1

print c

