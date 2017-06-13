cd = input("Enter current date")
cm = input("Enter current month")
cy = input("Enter current year")

dd = input("Enter birth date")
dm = input("Enter birth month")
dy = input("Enter birth year")

if cd >= dd:
	d = cd - dd

else:
	if cm in [1,3,5,7,8,10,12]:
		cd = cd + 31
	elif cm in [4,6,9,11]:
		cd = cd + 30
	elif cm == 2:
		if cd % 4== 0:
			cd = cd + 29
		else:
			cd = cd + 28
	d = cd - dd
	cm = cm - 1

if cm >= dm:
	m = cm - dm
else:
	cy = cy - 1
	cm = cm + 12
	m = cm - dm

y = cy - dy

print d,m,y
