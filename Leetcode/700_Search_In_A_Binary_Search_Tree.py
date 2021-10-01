# You are given the root of a binary search tree (BST) and an integer val.
# Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr = root
        
        while curr:
            if curr.val == val:
                return curr
            elif val > curr.val:
                curr = curr.right
            else:
                curr = curr.left
                
        return None
        

