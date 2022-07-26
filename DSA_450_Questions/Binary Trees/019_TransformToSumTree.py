## Given a Binary Tree of size N , where each node can have positive or negative values.
## Convert this to a tree where each node contains the sum of the left and right sub trees of the original tree.
## The value of leaf nodes are changed to 0

class Solution:
    def toSumTree(self, root) :
        if root is None:
            return 0
        l=self.toSumTree(root.left)
        r=self.toSumTree(root.right)
        old_value=root.data
        root.data=l+r
        return l+r+old_value


