## Given a binary tree of size N, find its reverse level order traversal. ie- the traversal must begin from the last level.

from collections import deque

def reverseLevelOrder(root):
    q = deque([root])
    ans = []
    
    if root is None:
        return None

    while len(q) > 0:
        curr = q.popleft()
        ans.append(curr.data)
        if curr.right is not None:
            q.append(curr.right)
        if curr.left is not None:
            q.append(curr.left)
    return ans[::-1]