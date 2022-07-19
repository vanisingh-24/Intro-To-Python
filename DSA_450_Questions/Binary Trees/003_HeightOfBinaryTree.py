## Given a binary tree, find its height.

class Solution:
    def height(self, root):
        if not root:
            return 0
        else:
            left = self.height(root.left)
            right = self.height(root.right)
            return 1 + max(left, right)