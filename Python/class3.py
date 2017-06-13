from class1 import create_node
from class1 import traverse

class xxx:
	data = None
	ad = None

def add_node(p):

	base = p
	pos = input("Enter the position : ")

	q = xxx()
	data = input("Enter the data : ")
	q.data = data

	if pos > 1:
		i = 1

		while i<pos-1:
			p = p.ad
			i+=1

		q.ad = p.ad
		p.ad = q

	elif pos == 1:
		q.ad = p
		base = q

	return base

def del_node(p):
	base = p

	q = xxx()
	pos = input("Enter the position to be deleted : ")

	if pos > 1:
		i = 1
		while i < pos - 1:
			p = p.ad
			i+=1

		p.ad = p.ad.ad

	elif pos == 1:
		base = p.ad
	return base


def main():
	base = create_node()
	traverse(base)
	base = add_node(base)
	traverse(base)
	base =  del_node(base)
	traverse(base)

main()