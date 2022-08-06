## Given a Binary Search Tree, modify the given BST such that itis balanced and has minimum possible height.

def buildBalancedTree(self,root):
        #code here
        ans = []
        self.inorder(root,ans)
        end = len(ans)
        return self.convert(ans,0 ,end-1)
def inorder(self,root,ans):
        if not root:
            return None
        self.inorder(root.left,ans)
        ans.append(root)
        self.inorder(root.right,ans)
    
def convert(self,ans,start,end):
        if start > end:
            return  None
        mid =  (start + end)//2
        root = (ans[mid])
        root.left = self.convert(ans,start,mid-1)
        root.right = self.convert(ans,mid+1, end)
        
        return root