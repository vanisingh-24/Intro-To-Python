## Given a Binary Tree. Check whether it is Symmetric or not, i.e. whether the binary tree is a Mirror image of itself or not.

class Solution:
    def isSymmetric(self, root):
        # Your Code Here
        if root is None:
            return True
        return (self.solve(root.left,root.right))
        
    def solve(self,left,right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.data!=right.data:
            return False
        return (self.solve(left.left,right.right)) and (self.solve(left.right,right.left))