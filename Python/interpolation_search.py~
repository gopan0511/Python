l = [11,22,33,44,55]

min = 0
max = len(l)-1

search = input("Enter the search element : ")

while min <= max and l[min] <= l[max] and search >= l[min] and search <= l[max]:
	mid = int(min + (float(max-min)/(l[max]-l[min])) * (search - l[min]))

	if search == l[mid]:
		print "Search is found"
		break

	elif search > l[mid]:
		min = mid+1

	elif search < l[mid]:
		max = mid-1

else:
	print "search is not found"
