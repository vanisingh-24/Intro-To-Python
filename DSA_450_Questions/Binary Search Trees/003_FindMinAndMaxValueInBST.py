## Given a Binary Search Tree. The task is to find the minimum element in this given BST.

def minValue(root):
    if not root:
        return -1
    if root.left is None:
        return root.data
    ans = minValue(root.left)
    return ans
