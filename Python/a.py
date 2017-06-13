#Program to convert uppercase to lowercase and lowercase to upercase
a = raw_input("Enter a string")
b = list(a)
c = []

for index in b:
	if(index.isupper()):
		c.append(index.lower())
	else:
		c.append(index.upper())

k = "".join(c)
print k