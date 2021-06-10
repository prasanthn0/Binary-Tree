from node import Node
from binary_tree import BinaryTree

tree=BinaryTree(Node(9))
tree.addNode(Node(11))
tree.addNode(Node(5))

tree.addNode(Node(4))
tree.addNode(Node(3))
tree.addNode(Node(2))
tree.addNode(Node(1))
tree.addNode(Node(6))

tree.inorder()
print('---')
print(tree.find(13))

