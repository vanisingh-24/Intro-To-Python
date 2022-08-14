## Given an array arr[] of N nodes representing preorder traversal of some BST.
## You have to build the exact BST from it's given preorder traversal. 
 
def post_order(pre, size) -> Node:
    root = Node(pre[0])
    for i in range(1, size):
        dfs(root, pre[i])
    return root
    
    
def dfs(root, val):
    if not root:
        return Node(val)
    if val < root.data:
        root.left = dfs(root.left, val)
    else:
        root.right = dfs(root.right, val)
    return root

# OR

def post_order(preorder, size) -> Node:
    inorder = sorted(preorder)

    def buildTree(preorder, inorder):
        if not preorder and not inorder:
            return None

        root = Node(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root
    
    return buildTree(preorder, inorder)