from node import Node


class BinaryTree:
    def __init__(self,head:Node):
        self.head=head


    def addNode(self,newNode:Node):
        current_node=self.head
        while current_node:
            if current_node.value==newNode.value:
                raise ValueError("A Node with that value already exists")

            elif newNode.value<current_node.value:
                if current_node.left:
                    current_node=current_node.left
                else:
                    current_node.left=newNode
                    break

            else:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right=newNode
                    break

    def inorder(self):
        self._inorder_recursive(self.head)

    def _inorder_recursive(self,current_node):

        if not current_node:
            return
        self._inorder_recursive(current_node.left)
        print(current_node)
        self._inorder_recursive(current_node.right)


    def find(self,value:int):
        current_node=self.head
        while current_node:
            if current_node.value==value:
                return current_node

            elif value > current_node.value:
                current_node=current_node.right

            else :
                current_node=current_node.left
        raise ValueError(f"A node with value {value} was not found!")


    def find_parent(self,value:int) -> node :
        current_node=self.head

        if self.head and self.head.value == value :
            return self.head

        """
        Above if is included because if head wants to be deleted , following while loop wont return the head
        
        
        
        """
        while current_node:
            if (current_node.left and current_node.left.value == value ) or\
                    ( current_node.right and current_node.right.value == value ):
                # or\ gives continuation in a conditional statement
                return current_node

            elif value < current_node.value:
                current_node = current_node.left

            else :
                current_node= current_node.right



    def find_rightmost(self,node:Node)->Node:
        current_node=node
        while current_node.right:
            current_node=current_node.right

        return current_node


    def delete_node(self,value:int):
        to_delete=self.find(value)
        to_delete_parent= self.find_parent(value)

        if to_delete_parent.left and to_delete_parent.right:
            # 2 children


        elif to_delete_parent.left or to_delete_parent.right  : # 1 child

            if to_delete_parent.left ==to_delete :
                to_delete_parent.left = to_delete.left or to_delete.right

            elif to_delete== to_delete_parent.right:
                to_delete_parent.right = to_delete.left or to_delete.right

            else:
                self.head=to_delete.left or to_delete.right



        else: #No child nodes
            if to_delete == to_delete_parent.left:
                to_delete_parent.left=None

            elif to_delete_parent.right == to_delete:
                to_delete_parent.right=None

            else:
                self.head=None










