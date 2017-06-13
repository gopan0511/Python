class node:
	data = None
	ad = None

def create_node():
	p = node()
	base = p 
	data = input('Enter data:')
	p.data = data
	while 1:
		print'1 for add node'
		print'0 for exit'
		ch = input('Enter ch:')

		if ch == 1:
			q = node()
			data = input('Enter data:')
			q.data = data

			p.ad = q
			p = q

		elif ch == 0:
			p.ad = 0
			break
		else:
			print'Invalid choice'
	return base

def traverse(p):
	while p != 0:
		print p.data
		p = p.ad

def main():
	base = create_node()
	traverse(base)

#main()
