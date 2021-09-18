# Given a binary tree, determine if it is height-balanced.

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def getDepth(node):
            if not node:
                return 0
            return 1 + max(getDepth(node.left), getDepth(node.right))
        
        if not root:
            return True
        return abs(getDepth(root.left) - getDepth(root.right)) <=1 and self.isBalanced(root.left) and self.isBalanced(root.right)

# OR

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]
            
            left , right = dfs(root.left), dfs(root.right)
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)
            
            return [balanced, 1 + max(left[1], right[1])]
        
        return dfs(root)[0]
        
