## There is BST given with root node with key part as an integer only.
## You need to find the in-order successor and predecessor of a given key.
## If either predecessor or successor is not found, then set it to NULL.

def findPreSuc(root, pre, suc, key):
    if root is None:
        return
    if root.key == key:
        if root.left:
            pre[0] = root.left
            while pre[0].right:
                pre[0] = pre[0].right
        if root.right:
            suc[0] = root.right
            while suc[0].left:
                suc[0] = suc[0].left
        return
    elif root.key < key:
        pre[0] = root
        findPreSuc(root.right, pre, suc, key)
    else:
        suc[0] = root
        findPreSuc(root.left, pre, suc, key)

