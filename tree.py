class Node:
	def __init__(self, left, right, data, label):
		self.left = left
		self.right = right
		self.data = data
		self.label = label
	
	def height(self):
		"""
			Height of the tree from given node to leaf
		"""
		if self.left != None and self.right != None:
			return 1 + max(self.left.height(), self.right.height())
		elif self.left != None:
			return 1 + self.left.height()
		elif self.right != None:
			return 1 + self.right.height()
		else:
			return 0

	def inorder(self):
		"""
			In Order Traversal of tree
		"""
		if self.left != None:
			self.left.inorder()
		print(self.label)
		if self.right != None:
			self.right.inorder()
	
	def preorder(self):
		"""
			Pre Order Traversal
		"""
		print(self.label)
		if self.left != None:
			self.left.preorder()
		if self.right != None:
			self.right.preorder()

	def postorder(self):
		"""
			Post Order Traversal
		"""
		if self.left != None:
			self.left.postorder()
		if self.right != None:
			self.right.postorder()
		print(self.label)

	def levelorder(self):
		"""
			level order traversal. Implemented using a queue. 
		"""
		q = [self]
		while q:
			currNode = q.pop(0)
			print(currNode.label)
			if currNode.left != None:
				q.append(currNode.left)
			if currNode.right != None:
				q.append(currNode.right)
		return

	

# Tests
N = Node(None, None, 257, "N")
M = Node(None, None, 641, "M")
D = Node(None, None, 28, "D")
E = Node(None, None, 0, "E")
P = Node(None, None, 28, "P")
H = Node(None, None, 17, "H")

L = Node(None, M, 401, "L")
K = Node(L, N, 1, "K")
O = Node(None, P, 271, "O")
G = Node(H, None, 3, "G")
F = Node(None, G, 561, "F")
J = Node(None, K, 2, "J")
C= Node(D, E, 271, "C")



B = Node(C, F, 6, "B")
I = Node(J, O, 6, "I")
root = Node(B, I, 314, "A")


print(root.levelorder())
