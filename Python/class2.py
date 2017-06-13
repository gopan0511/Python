from class1 import create_node
from class1 import traverse

def rev_linkedlist(p):

	pre=0
	post=0
	
	while p.ad!=0:
		post=p.ad
		p.ad=pre
		pre=p
		p=post
	p.ad=pre
	
	return p

def main():

	base=create_node()
	traverse(base)

	print 'the linked list is reversed'

	base=rev_linkedlist(base)
	traverse(base)

main()
