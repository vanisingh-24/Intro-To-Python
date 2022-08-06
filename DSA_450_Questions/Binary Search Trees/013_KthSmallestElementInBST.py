## Given a BST and an integer K. Find the Kth Smallest element in the BST. 

def inorder(self, root, a):
        if root is None:
            return
        self.inorder(root.left, a)
        a.append(root.data)
        self.inorder(root.right, a)
        
def KthSmallestElement(self,root, K):
        a = []
        self.inorder(root, a)
        if K > len(a):
            return -1
        return a[K-1]