arr = input("Enter the array : ")
maxval = input("Enter the maximum value of the array : ")

def countingSort(arr,maxval):
	 
	m = maxval+1
	count = [0] * m #initialise the count array with 0

	for a in arr:
		count[a] += 1 #count the number of occurences

	i = 0
	for a in range(m):
		for c in range(count[a]):
			arr[i] = a
			i += 1

	return arr

countingSort(arr,maxval)
print(arr)
	
	
	
