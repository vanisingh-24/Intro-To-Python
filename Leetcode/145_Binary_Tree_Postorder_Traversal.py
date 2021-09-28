# Given the root of a binary tree, return the postorder traversal of its nodes' values.

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        
        def helper(node):
            if not node:
                return None
            
            helper(node.left)
            helper(node.right)
            output.append(node.val)
            
        helper(root)
        return output