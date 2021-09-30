# Given the root of a binary tree, invert the tree, and return its root.

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        
        r = self.invertTree(root.right)
        l = self.invertTree(root.left)
        
        root.right = l
        root.left = r
        
        return root

