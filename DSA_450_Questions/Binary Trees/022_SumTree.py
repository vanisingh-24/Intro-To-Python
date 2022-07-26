## Given a Binary Tree. Return true if, for every node X in the tree other than the leaves, its value is equal to the sum of its left subtree's value and its right subtree's value. Else return false.
## An empty tree is also a Sum Tree as the sum of an empty tree can be considered to be 0. A leaf node is also considered a Sum Tree.

def sum(self,root):
        if root==None:
            return 0
        return (self.sum(root.left)+root.data+self.sum(root.right))
    
def isSumTree(self,root):
        # Code here
        if root==None or root.left==None or root.right==None:
            return 1
        ls=self.sum(root.left)
        rs=self.sum(root.right)
        if root.data==ls+rs and self.isSumTree(root.left) and self.isSumTree(root.right):
            return 1
        else:
            return 0

