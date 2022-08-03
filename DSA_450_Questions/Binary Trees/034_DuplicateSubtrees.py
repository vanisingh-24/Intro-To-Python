## Given a binary tree of size N, your task is to that find all duplicate subtrees from the given binary tree.

def printAllDups(self,root):
        
        def solve(root):
            if not root:
                return '$'
            s = ''
            l = solve(root.left)
            r = solve(root.right)
            s = l + ',' + r + ',' + str(root.data)
            if s in m:
                m[s] += 1
            else:
                m[s] = 1
            if m[s] == 2:
                res.append(root)
            return s 
            
        m = {}
        res= []
        solve(root)
        return res