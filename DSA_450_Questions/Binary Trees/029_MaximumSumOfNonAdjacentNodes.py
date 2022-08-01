## Given a binary tree with a value associated with each node, we need to choose a subset of these nodes such that sum of chosen nodes is maximum under a constraint that no two chosen node in subset should be directly connected that is, if we have taken a node in our sum then we can’t take its any children or parents in consideration and vice versa.

def getMaxSum(self, root):
        ans = self.test(root)
        return max(ans[0], ans[1])
        
def test(self, root):
        if root is None:
            return [0, 0]
            
        left = self.test( root.left)
        right = self.test( root.right)
        
        l = max(left[0], left[1]) + max(right[0], right[1])
        r = left[1] + right[1] + root.data
        
        return [r, l]