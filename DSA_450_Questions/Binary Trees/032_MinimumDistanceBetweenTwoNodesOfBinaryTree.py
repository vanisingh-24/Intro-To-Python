## Given a binary tree and two node values your task is to find the minimum distance between them.

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
            
def findDistanceFromLCA(self,root,d):
        if root == None:
            return -1
        if root.data==d:
            return 0
        left = self.findDistanceFromLCA(root.left,d)
        right = self.findDistanceFromLCA(root.right,d)
        distance = max(left,right)
        return distance+1 if distance>=0 else -1
        
def findDist(self,root,a,b):
        root = self.lca(root,a,b)
        d1 = self.findDistanceFromLCA(root,a)
        d2 = self.findDistanceFromLCA(root,b)
        return d1+d2
        