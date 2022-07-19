## Given a Binary Tree, convert it into its mirror.

class Solution:
    def mirror(self,root):
        if not root:
            return 
        
        root.left, root.right = root.right, root.left
        
        self.mirror(root.left)
        self.mirror(root.right)
        
        return root