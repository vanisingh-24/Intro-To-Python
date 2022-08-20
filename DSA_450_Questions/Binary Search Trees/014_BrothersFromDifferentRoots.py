## Given two BSTs containing N1 and N2 distinct nodes respectively and given a value x.
## Your task is to complete the function countPairs(), that returns the count of all pairs from both the BSTs whose sum is equal to x.

def countPairs(self, root1, root2, x): 
        d1 = {}
        d2 = {}
        self.inorder(root1, d1)
        self.inorder(root2, d2)
        ans = 0
        for i in d1:
            if x-i in d2:
                ans += 1
        return ans
        
def inorder(self, root, d):
        if root:
            self.inorder(root.left, d)
            d[root.data] = 1
            self.inorder(root.right, d)