## Given the root of a binary tree. Check whether it is a BST or not.

def isBST(self, root):
        def valid(node, left, right):
            if not node:
                return 1
            elif node.data <= left or node.data >= right:
                return 0
            else:    
                return valid(node.left,left,node.data) and valid(node.right,node.data,right)
        return valid(root, float('-inf'),float('inf'))

