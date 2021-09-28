# Given the root of a binary tree, return the preorder traversal of its nodes' values.

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        
        def helper(node):
            if not node:
                return None
            
            output.append(node.val)
            helper(node.left)
            helper(node.right)
            
        helper(root)
        return output

