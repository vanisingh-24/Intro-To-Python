## Given a Binary Search Tree and a node value X.
## Delete the node with the given value X from the BST.
## If no node with value x exists, then do not make any change. 

def deleteNode(root, X):
    if not root:
        return None
        
    if root.data == X:
        if not root.left and not root.right:
            return None
        if not root.left and root.right:
            return root.right
        if not root.right and root.left:
            return root.left
        temp = root.right
        while temp.left:
            temp = temp.left
        root.data = temp.data
        root.right = deleteNode(root.right, root.data)
        
    elif root.data > X:
        root.left = deleteNode(root.left, X)
    else:
        root.right = deleteNode(root.right, X)
    return root