## Given a Binary Tree (BT), convert it to a Doubly Linked List(DLL) In-Place.
## The left and right pointers in nodes are to be used as previous and next pointers respectively in converted DLL. 
## The order of nodes in DLL must be same as Inorder of the given Binary Tree.
## The first node of Inorder traversal (leftmost node in BT) must be the head node of the DLL.

class Solution:
    def inorder(self,root):
        if root==None:
            return 
        self.inorder(root.left)
        if self.prev==None:
            self.head=root
        else:
            root.left = self.prev
            self.prev.right = root
        self.prev = root
        self.inorder(root.right)
        return None
        
    def bToDLL(self,root):
        # do Code here
        self.prev = None
        self.head = None
        self.inorder(root)
        return self.head