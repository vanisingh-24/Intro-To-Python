# Given the root of a binary tree, return the inorder traversal of its nodes' values.

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Iterative way
        output = []
        stack = []
        
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                holder = stack.pop()
                output.append(holder.val)
                root = holder.right
                
        return output
        
# OR

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Recursive Solution
        output = []
        
        def helper(node):
            if not node:
                return
            
            helper(node.left)
            output.append(node.val)
            helper(node.right)
            
        helper(root)
        return output
        