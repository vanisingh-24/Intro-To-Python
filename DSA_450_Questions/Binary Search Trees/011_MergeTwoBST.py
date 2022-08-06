## Given two BSTs, return elements of both BSTs in sorted form.

def inorder(self, root1, ans):
        if root1 == None:
            return
        self.inorder(root1.left, ans)
        ans.append(root1.data)
        self.inorder(root1.right, ans)
           
def merge(self, root1, root2):
        ans = []
        self.inorder(root1, ans)
        self.inorder(root2, ans)
        ans.sort()
        return ans