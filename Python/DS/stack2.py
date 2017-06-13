class Stack(object):
	
	def __init__(self,limit = 10):
		self.stk = [None]*limit
		self.limit = limit

	def isEmpty(self):
		return len(self.stk) <= 0

	def push(self,item):
		if len(self.stk) >= self.limit:
			self.resize()
		self.stk.append(item)
		print 'Stack afte PUSH operation',self.stk

	def pop(self):
		if len(self.stk) <= 0:
			print 'STACK UNDERFLOW'
			return 0
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
	
	def resize(self):
		newStack = list(self.stk)
		self.limit = 2*self.limit
		self.stk = newStack

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
stack.push("20")
stack.push("12")
stack.push("34")
stack.push("11")
stack.push("98")
stack.push("44")
print stack.peek()
print stack.pop()
print stack.peek()
print stack.pop()

stack.printStack()
                  
