## The task is to print the top view of binary tree. Top view of a binary tree is the set of nodes visible when the tree is viewed from the top

def topView(self,root):
        d = {}
        q = [(0, root)]
        res = []
        
        while q:
            for i in range(len(q)):
                h, node = q.pop(0)
                if h not in d:
                    d[h] = node.data
                if node.left:
                    q.append((h-1,node.left))
                if node.right:
                    q.append((h+1, node.right))
        
        for i in sorted(d.keys()):
            res.append(d[i])
        return res


 