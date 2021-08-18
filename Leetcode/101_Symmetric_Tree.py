# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        return self.isMirror(root, root)
    def isMirror(self, left, right):
        if left == None and right == None:
            return True
        elif left == None or right == None:
            return False
        else:
            return left.val == right.val and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)