class Queue:
    def __init__(self):
        self.items=[]

    def push(self,e):
        self.items.append(e)

    def pop(self):
        head=self.items[0]
        self.items=self.items[1:]
        return head


class Stack:
    def __init__(self):
        self.items=[]

    def push(self,e):
        self.items=[e]+self.items

    def pop(self):
        return self.items.pop()

"""
1. SEQUENTIAL : 
        Cant pop an element unless all other preceeding elements are popped first.

"""

#Binary Search :
#Find 90 :

target=[1,2,3,4,5,6,23,34,56,57,67,68,69,70,71,90,91,92,93,100,121]

"""
Method: ----ORDERED / SORTED LIST----
    Start in middle , find  target[mid].
    Compare target[mid] > 90.
    If No , discard all lower elements , else discard all greater elements.
    
    Now go to middle elements in whats remaining and repeat method above.
    
    This will tae us 4 jumps but sequentially it would have taken 16 jumps.
    
    log(21)(base 2) = 4.39
    Therefore complexity is O(logN)
    
    This is Binary search : It lets us make a decision between 2 choices at every jump i.e., go left or go right.
    
  This in tree from is a binary tree!
  
  Traversal:
  1. Inorder traversal : go left first, check node and then go right.
  2. Preorder traversal : check node first , then decide which direction.
  3. Postorder traversal : go left first, go right next and then check node.  
    
"""

def add_node():
    new_node=Node(value=5,left=None,right=None) # A node has 3 properties : value and left and right branch values.
    current_node=self.head   # Start from the root or the head
    while current_node :  # Because we dont know how many nodes we might traverse
        if new_node.value==current_node.value:
            raise ValueError("A node with that Value already exists!")
        elif new_node.value < current_node.value:
            if current_node.left:
                current_node=current_node.left
            else:
                current_node.left=new_node
                break
        elif new_node.value > current_node.value:
            if current_node.right:
                current_node=current_node.right
            else:
                current_node.right=new_node
                break

"""
Python will erase something from memory when it doesnt have any link to any code or pointed to..

So in order to delete a child node,  removing the link is enough i.e., node.left=None

But what if the node getting deleted has children?

case 1: No children : Point the previous node to None

case 2: Has 1 child : Point the previous node to the child node of delinked node.

case 3: has 2 children : 

            Example :
            
            root node :  6
                                   9
                            
                              7         12
                            
                                 8   11
                               
        9 has 2 branches with ( 7 ,8 ) and (12, 11) . Lets say we want to delete 9 . Then in such a case
        :7 cannot replace 9 since 7 already has a right node and if it replaces 9 , it will have to have
        2 right nodes which is not possible.
        :12 cannot replace 9 since because it already has a left node and 7 will becomes another left node which
        again is not possible.
        
        But 8 cann replace 9 because 7 can become its left node and 12 can become its right ode without any
        contradiction.
        Similarly, 11 is fine too.
        
        Observation : Pick the biggest node in the left branch i.e., right most node in left branch or
                      Pick the smallest node in the right branch i.e., left most node is right branch.
                      
        
        
        


"""