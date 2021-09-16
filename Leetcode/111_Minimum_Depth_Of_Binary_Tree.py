# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # for empty node or empty tree
        if not root:
            return 0
        
        # leaf node
        if not root.left and not root.right:
            return 1
        
        # only has left sub-tree
        elif not root.right:
            return self.minDepth(root.left) + 1
        
        # only has right sub-tree
        elif not root.left:
            return self.minDepth(root.right) + 1
        
        # # has left sub-tree and right sub-tree
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

