#Python implementation of Binary Index Tree

def getsum(BITree, i):
	s = 0 #initialise result

	i = i + 1#index in binary tree is one more than that of an array

	while i > 0:
		s += BITree[i]
		#move index to parent node in getSum view
		i -= i &(-i)
	return s

def updatebit(BITree, n, i, v):
	i += 1

	while i<=n:
		BITree[i] += v
		i += i & (-i)

def construct(arr,n):
	#create and initialise BITree[] as 0
	BITree = [0]*(n+1)

	for i in range(n):
		updatebit(BITree,n,i,arr[i])

	return BITree

freq = [2,1,1,3,2,3,4,5,6,7,8,9]
BITree = construct(freq,len(freq))
print("Sum of elements in arr[0..5] is " + str(getsum(BITree,5)))
freq[3] += 6
updatebit(BITree,len(freq),3,6)
print("Sum of elements in arr[0..5] is " + str(getsum(BITree,5)))
