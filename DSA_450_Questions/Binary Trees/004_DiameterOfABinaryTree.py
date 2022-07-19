## The diameter of a tree (sometimes called the width) is the number of nodes on the longest path between two end nodes.

class Solution:
    def diameter(self,root):
        res = [0]
        
        def height(root):
            if not root:
                return -1
            left = height(root.left)
            right = height(root.right)
            res[0] = max(res[0], 2 + left + right)
            
            return 1 + max(left, right)
            
        height(root)
        return res[0]+1

