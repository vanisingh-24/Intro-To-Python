## Given a Binary Tree, print the diagonal traversal of the binary tree.

def diagonal(self,root):
        res = []
        q = [root]
        
        while q:
            temp = q.pop(0)
            while temp:
                if temp.left:
                    q.append(temp.left)
                res.append(temp.data)
                temp = temp.right
        return res 