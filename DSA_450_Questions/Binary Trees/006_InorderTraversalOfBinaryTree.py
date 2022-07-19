## Given a Binary Tree, find the In-Order Traversal of it.

# Recursive Approach

class Solution:
    def InOrder(self,root):
        if not root:
            return []
        res = []
        res += self.InOrder(root.left)
        res.append(root.data)
        res += self.InOrder(root.right)
        return res

# Iterative Approach

class Solution:
    def inOrder(self, root):
        res = []
        stack = []
        
        while True:
            if root is not None:
                stack.append(root)
                root = root.left
            elif(stack):
                temp = stack.pop()
                res.append(temp.data)
                root = temp.right
            else:
                break
        return res

