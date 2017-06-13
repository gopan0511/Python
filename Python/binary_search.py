l = [11,22,33,44,55]

min = 0
max = len(l)-1

search = input("Enter the search element : ")

while min <= max:
	mid =  (min+max)/2

	if search == l[mid]:
		print "Search is found"
		break

	elif search > l[mid]:
		min = mid+1

	elif search < l[mid]:
		max = mid-1

else:
	print "search is not found"
