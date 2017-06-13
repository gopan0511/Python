class Stack:
	
	def __init__(self):
		self.items = []
	#method for pushing an item on a stack
	def push(self,item):
		self.items.append(item)
	#method for popping an item on a stack
	def pop(self):
		return self.items.pop()

	#method to check whether stack is empty
	def isEmpty(self):
		return (self.items == [])
	
	def __str__(self):
		return str(self.items)
	#method to get the top of the stack
	def peek(self):
		return self.items[-1]

def infixToPostfix(infix):
	prec = {}  #use of dictionary to access through key
	prec["*"] = 3
	prec["/"] = 3
	prec["+"] = 2
	prec["-"] = 2
	prec["("] = 1
	opStack = Stack()
	postfix = []
	tokenList = infix.split()

	for token in tokenList:
		if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789" or token in "abcdefghijklmnopqrstuvwxyz":
			postfix.append(token)
		elif token == '(':
			opStack.push(token)
		elif token == ')':
			topToken = opStack.pop()
			while topToken != '(':
				postfix.append(topToken)
				topToken = opStack.pop()
		else:
			while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
				postfix.append(opStack.pop())
			opStack.push(token)
	while not opStack.isEmpty():
		postfix.append(opStack.pop())
	
	return " ".join(postfix)

print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
