# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from Stack import Stack

class BinaryNode:
	value = None
	leftChild = None
	rightChild = None

	def __init__(self,val,lChild = None,rChild = None):
		self.value = val
		self.leftChild = lChild
		self.rightChild = rChild

class BinaryTree:
	root = None
	def __init__(self,rootNode):
		self.root = rootNode

	@staticmethod
	def _visit(node):
		print node.value

	@staticmethod
	def preorder(rootNode):
		s = Stack()
		p = rootNode

		while(p or (not s.empty())):
			if p:
				BinaryTree._visit(p)
				if p.rightChild:
					s.push(p.rightChild)
				p = p.leftChild
			else:
				p = s.pop()
	@staticmethod
	def inorder(rootNode):
		s = Stack()
		p = rootNode
		while(p or (not s.empty())):
			if p:
				s.push()
				p = p.leftChild
			else:
				p = s.pop()
				BinaryTree._visit(p)
				p = p.leftChild
	@staticmethod
	def postorder(rootNode):
		s = Stack()
		p = rootNode
		lastVisit = None
		s.push()
		while(not s.empty()):
			p = s.top()
			#case1: the right child is visited, so left child must be visited
			#case2: left and right child are all null
			#case3: the left child is visited and the right child is null
			if(p.rightChild == lastVisit)or(p.rightChild == None and p.leftChild == None)or(p.rightChild == None and p.leftChild == lastVisit):
				BinaryTree._visit(p)
				lastVisit = p
				s.pop()
			else:
				if(p.rightChild):
					s.push(p.rightChild)
				if(p.leftChild):
					s.push(p.leftChild)
	def preorderWalk(self):
		BinaryTree.preorderTraverse(self.root) 

	def inorderWalk(self):
		BinaryTree.inorderTraverse(self.root)

	def postorderWalk(self):
		BinaryTree.postorderTraverse(self.root)

b = BinaryNode(1,BinaryNode(2,BinaryNode(4),BinaryNode(5,BinaryNode(8))),BinaryNode(3,BinaryNode(6),BinaryNode(7,None,BinaryNode(9))))

t = BinaryTree(b)
print "preorder"
t.preorderWalk()

print "inorder"
t.inorderWalk()

print "postorder"
t.postorderWalk()