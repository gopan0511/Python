time = input("Enter time: ")
if time >= 8 and time <= 16:
	print "valid time"
	
	if time == 8:
		pay = 200
	
	elif time > 8 and time <=12:
		pay = 200 + (time - 8)*100
	
	elif time > 12 and time <=16:
		pay = 600 + (time -12)*200
	
	print pay
	
else:
	print "invalid time"
