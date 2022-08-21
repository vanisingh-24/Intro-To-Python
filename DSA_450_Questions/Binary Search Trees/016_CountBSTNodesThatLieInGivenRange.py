## Given a Binary Search Tree (BST) and a range l-h(inclusive), count the number of nodes in the BST that lie in the given range.
## The values smaller than root go to the left side
## The values greater and equal to the root go to the right side


def getCount(self,root,low,high):
        if not root:
            return 0
        ans = 0
        ans += self.getCount(root.left, low, high)
        if low <= root.data <= high:
            ans += 1
        ans += self.getCount(root.right, low, high)
        return ans
    
def getCount(self,root,low,high):
        if root==None:
            return 0
        x=0
        if root.data>=low and root.data<=high:
            x+=1
        left=self.getCount(root.left,low,high)
        right=self.getCount(root.right,low,high)
        return left+right+x