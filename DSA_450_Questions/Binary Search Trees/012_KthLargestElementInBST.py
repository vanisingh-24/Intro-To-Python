## Given a Binary search tree.
## Your task is to complete the function which will return the Kth largest element without doing any modification in Binary Search Tree.

def inorder(self, root, a):
        if root is None:
            return
        self.inorder(root.left, a)
        a.append(root.data)
        self.inorder(root.right, a)
        
def kthLargest(self,root, k):
        a = []
        self.inorder(root, a)
        a.reverse()
        return a[k-1]
        