## Given a binary tree and an integer K. Find the number of paths in the tree which have their sum equal to K.
## A path may start from any node and end at any node in the downward direction.

import collections
def sumK(self,root,k):
        self.total = 0
        self.d = defaultdict(int)
        self.d[k] = 1
        def dfs(node, sum):
            if not node:
                return
            sum += node.data
            self.total += self.d[sum]
            self.d[sum+k] += 1
            dfs(node.left, sum)
            dfs(node.right, sum)
            self.d[sum+k] -= 1
            
        dfs(root, 0)
        return self.total
        