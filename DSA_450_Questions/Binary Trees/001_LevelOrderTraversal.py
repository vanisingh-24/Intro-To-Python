## Given a binary tree, find its level order traversal.
## Level order traversal of a tree is breadth-first traversal for the tree.

from collections import deque

class Solution:
    def levelOrder(self,root ):
        if root is None:
            return None
        q = deque([root])
        ans = []
        while len(q) > 0:
            curr = q.popleft()
            ans.append(curr.data)
            if curr.left is not None:
                q.append(curr.left)
            if curr.right is not None:
                q.append(curr.right)
        return ans
