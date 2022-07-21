## Given a Binary Tree, print Left view of it. Left view of a Binary Tree is set of nodes visible when tree is visited from Left side.
## The task is to complete the function leftView(), which accepts root of the tree as argument.

import collections
def LeftView(root):
    res = []
    q = collections.deque([root])
    while q:
        leftSide = None
        level = len(q)
        for i in range(level):
            node = q.popleft()
            if node:
                leftSide = node
                q.append(node.right)
                q.append(node.left)
        if leftSide:
            res.append(leftSide.data)
    return res

# OR

def LeftView(root):
    def left(root, level, max_level):
        if root is None:
            return
        if len(max_level)==level:
            max_level.append(root.data)
        left(root.left,level+1,max_level)
        left(root.right,level+1,max_level)
    max_level = []
    left(root, 0, max_level)
    return max_level
