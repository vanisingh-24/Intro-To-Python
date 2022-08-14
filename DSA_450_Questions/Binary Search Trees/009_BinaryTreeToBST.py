## Given a Binary Tree, convert it to Binary Search Tree in such a way that keeps the original structure of Binary Tree intact.

def inorder(self,root,arr):
        if root is None:
            return 
        self.inorder(root.left,arr)
        arr.append(root.data)
        self.inorder(root.right,arr)
        return arr
        
def traverse(self,root,arr):
        if root is None:
            return
        self.traverse(root.left,arr)
        root.data=arr[0]
        arr.pop(0)
        self.traverse(root.right,arr)
        return root
    
def binaryTreeToBST(self, root):
        # code here
        if root is None:
            return None
        arr=[]
        self.inorder(root,arr)
        arr.sort()
        return self.traverse(root,arr)