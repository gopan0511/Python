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

def matches(open,close):
	opens = "([{"
	closers = ")]}"
	return opens.index(open) == closers.index(close)

def checkSymbolBalance(input):
	symbolstack = Stack()
	balanced = 0
	
	for symbols in input:		
		if symbols in ["(","[","{"]:
			symbolstack.push(symbols)
		else:
			if symbolstack.isEmpty():
				balanced = 0
			else:
				topSymbol = symbolstack.pop()
				if not matches(topSymbol,symbols):
					balanced = 0
				else:
					balanced = 1
	return balanced

print checkSymbolBalance("([)]")
print checkSymbolBalance("{{([][])}}")
