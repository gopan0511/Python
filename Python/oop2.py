class xxx:
	name = None
	id = None
	def __init__(self,name,id):
		print 'I am a constructor'
		self.name = name
		self.id = id
	def __del__(self):
		print 'I am a Destructor'

	def show(self):
		print self.name
		print self.id
	
x = xxx("Gopan",1234)
x.show()

