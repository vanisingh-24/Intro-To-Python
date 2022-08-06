## Given a Binary Tree, write a function to populate next pointer for all nodes.
## The next pointer for every node should be set to point to inorder successor.

def inorder(root, prev):
    if root is None:
        return
    inorder(root.left, prev)
    if prev is not None:
        prev.next = root
    prev = root
    inorder(root.right, prev)
    
def populateNext(root):
    prev = None
    inorder(root, prev)
    return 
        