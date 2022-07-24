## Given a binary tree, print the bottom view from left to right.

def bottomView(self, root):
        d = {}
        q = [(0, root)]
        res = []
        
        while q:
            for i in range(len(q)):
                h, node = q.pop(0)
                d[h] = node.data
                if node.left:
                    q.append((h-1, node.left))
                if node.right:
                    q.append((h+1, node.right))
                    
        for i in sorted(d.keys()):
            res.append(d[i])
        return res