## Given a Binary Tree, find its Boundary Traversal.

def printBoundaryView(self, root):
        def leftTraversal(root, ans):
            if root:
                if root.left:
                    ans.append(root.data)
                    leftTraversal(root.left, ans)
        
                elif root.right:
                    ans.append(root.data)
                    leftTraversal(root.right, ans)
        
        
        def leafTraversal(root, ans):
            if root:
                leafTraversal(root.left, ans)
                if root.left == None and root.right == None:
                    ans.append(root.data)
                leafTraversal(root.right, ans)
        
        
        def rightTraversal(root, ans):
            if root:
                if root.right:
                    rightTraversal(root.right, ans)
                    ans.append(root.data)
        
                elif root.left:
                    rightTraversal(root.left, ans)
                    ans.append(root.data)
            
        if root == None:
            return []
        ans = [root.data]
        leftTraversal(root.left, ans)
        leafTraversal(root.left, ans)
        leafTraversal(root.right,ans)
        rightTraversal(root.right, ans)
        return ans
