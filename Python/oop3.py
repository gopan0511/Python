class student:
	name = None
	id = None

	def __init__(self,name,id):
		self.name = name
		self.id = id
		

	def store(self,f_name):
		#store the name and id of the student in student.txt
		line_write = self.name+'\t'+str(self.id)+'\n'
		fo = open(f_name,'a')
		fo.write(line_write)
		fo.close()	


class emp(student):
	name = None
	id = None
	salary = None	

	def __init__(self,name,id,salary):
		student.__init__(self,name,id)
		self.salary = salary

	
		
s1 = student('Gopan',11)
e = emp('ABCDE',1190290,100000)

s2 = student('Himanshu',12)
s3 = student('Hassan',13)
s4 = student('Elson',14)
s1.store('student.txt')
s2.store('student.txt')
s3.store('student.txt')
s4.store('student.txt')

e.store('emp.txt')
