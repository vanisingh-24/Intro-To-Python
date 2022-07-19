## Given a Binary Tree, find the Pre-Order Traversal of it.

# Recursive Approach

def preorder(root):
    if not root:
        return []
    res = []
    res.append(root.data)
    res += preorder(root.left)
    res += preorder(root.right)
    return res

# Iterative Approach

class Solution:
    def preOrder(self, root):
        res = []
        stack = [root]
        
        if root is None:
            return
        while stack:
            temp = stack.pop()
            res.append(temp.data)
            if temp.right:
                stack.append(temp.right)
            if temp.left:
                stack.append(temp.left)
        return res