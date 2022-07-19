## Given a Binary Tree, find the Post-Order Traversal of it.

# Recursive Approach

def postOrder(root):
    if not root:
        return []
    res = []
    res += postOrder(root.left)
    res += postOrder(root.right)
    res.append(root.data)
    return res

# Iterative Approach

class Solution:
    def postOrder(self, root):
        if root is None:
            return []
            
        stack = [root]
        res = []
        while (stack): 
            temp = stack.pop()
            if temp.left:
                stack.append(temp.left)
            if temp.right:
                stack.append(temp.right)
            res.append(temp.data)
        return res[::-1]