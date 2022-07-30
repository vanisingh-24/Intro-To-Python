## Given 2 Arrays of Inorder and preorder traversal. Construct a tree and print the Postorder traversal. 

def buildtree(self, inorder, preorder, n):
        def helper(inorder,preorder):
            if not preorder or not inorder:
                return None
            root=Node(preorder[0])
            mid=inorder.index(preorder[0])
            root.left=helper(inorder[:mid],preorder[1:mid+1])
            root.right=helper(inorder[mid+1:],preorder[mid+1:])
            return root
        
        return helper(inorder,preorder)