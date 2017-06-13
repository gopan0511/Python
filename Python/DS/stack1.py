class Stack(object):
	
	def __init__(self,limit = 10):
		self.stk = []
		self.limit = limit
	
	def isEmpty(self):
		return len(self.stk) <= 0
	
	def push(self,item):
		if len(self.stk) >= self.limit:
			print 'STACK OVERFLOW'
		else:
			self.stk.append(item)
		print 'Stack after push',self.stk

	def pop(self):
		if len(self.stk) <= 0:
			print 'STACK UNDERFLOW'
		else:
			return self.stk.pop()

	def peek(self):
		if len(self.stk) <= 0:
			print 'STACK UNDERFLOW'
			return 0
		else:
			return self.stk[-1]

	def size(self):
		return len(self.stk)

	def printStack(self):
		print self.stk

stack = Stack(5)
stack.push("1")
stack.push("21")
stack.push("14")
stack.push("31")
stack.push("19")
stack.push("3")
stack.push("99")
stack.push("9")
print stack.peek()
print stack.pop()
print stack.peek()
print stack.pop()
	
stack.printStack()
