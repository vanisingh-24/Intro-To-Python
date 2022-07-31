## Given a binary tree, find out whether it contains a duplicate sub-tree of size two or more, or not.

def dupSub(self, root):
        m = {}
        def solve(root):
            if not root:
                return "$"
            s = ""
            if not root.left and not root.right:
                s = str(root.data)
                return s
            s += str(root.data)
            s += solve(root.left)
            s += solve(root.right)
            if s in m:
                m[s] += 1
            else:
                m[s] = 1
        
            return s
        solve(root)
        for i in m:
            if (m[i] >= 2):
                return 1
        return 0 