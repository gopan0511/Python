class xxx:
	data = None


def main():
	p = xxx()

	base = p

	data = input("Enter the data : ")

	p.data = data

	while 1:
		print '1 for add a node'
		print '0 for exit'

		ch = input("Enter a choice")

		if ch == 1:
			q = xxx()
			data = input("Enter the data : ")
			q.data = data
			p.next = q
			p = q

		elif ch == 0:
			p.next = 0
			break
		else:
			print 'invalid choice'

	p = base
	while p != 0:
		print p.data
		p = p.next

main()