## Given a Binary Tree with all unique values and two nodes value, n1 and n2.
## The task is to find the lowest common ancestor of the given two nodes.
## We may assume that either both n1 and n2 are present in the tree or none of them are present.

# Using Single Traversal

def lca(self,root, n1, n2):
        if root is None:
            return None
        if root.data == n1 or root.data == n2:
            return root
        l = self.lca(root.left, n1, n2)
        r = self.lca(root.right, n1, n2)
        if l != None and r != None:
            return root
        elif l!= None:
            return l
        else:
            return r