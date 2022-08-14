## Given a Binary Search Tree (with all values unique) and two node values. 
## Find the Lowest Common Ancestors of the two nodes in the BST.

# Using dfs

def LCA(root, n1, n2):
    def dfs(node, t1, t2):
        if not node:
            return None
        if node.data == t1 or node.data == t2:
            return Node
        left = dfs(node.left, n1, n2)
        right = dfs(node.right, n1, n2)
        
        if left and right:
            return node
        return left or right
    return dfs(root, n1, n2)

# Recursion

def lca(root, n1, n2):
    if not root:
        return None
    if root.data > n1 and root.data > n2:
        return lca(root.left, n1, n2)
    elif root.data < n1 and root.data < n2:
        return lca(root.right, n1, n2)
    else:
        return root