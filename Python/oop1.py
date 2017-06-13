def bbsr(y):
	print y.data
	print 'hello bbsr'

class xxx:
	data = None
	
	def hello(xyz):
		#print self.data
		print 'Hello'

x = xxx()
#xxx.hello() remove self from the hello() in class xxx.
print x.data
x.name = 'GOPAN'
print x.name
x.data = 1000
print x.data

y = xxx()
y.data = 2000
y.hello()
y.bbsr = bbsr
y.bbsr(y)
