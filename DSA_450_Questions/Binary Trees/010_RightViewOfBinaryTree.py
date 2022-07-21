## Given a Binary Tree, find Right view of it. Right view of a Binary Tree is set of nodes visible when tree is viewed from right side.

import collections
class Solution:
    def rightView(self,root):
        res = []
        q = collections.deque([root])
        while q:
            rightSide = None
            level = len(q)
            for i in range(level):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.data)
        return res
    
# OR

class Solution:
    def rightView(self,root):
        def right(root, level, max_level):
            if root != None:
                if len(max_level) == level:
                    max_level.append(root.data)
                
                right(root.right, level+1, max_level)
                right(root.left, level+1, max_level)
        max_level = []
        right(root, 0, max_level)
        return max_level