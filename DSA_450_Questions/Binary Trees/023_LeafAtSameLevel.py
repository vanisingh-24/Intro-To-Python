## Given a Binary Tree, check if all leaves are at same level or not.

def check(self, root):
        level=0
        a=set()
        self.checklevel(root,level,a)
        if len(a)==1:
            return 1
        else:
            return 0
        
def checklevel(self,root,level,a):
        if root==None:
            return 1
        if root.left is None and root.right is None:
            a.add(level)
            return
            
        self.checklevel(root.left,level+1,a)
        self.checklevel(root.right,level+1,a)
        
# Alternate Solution

def check(self,root):
        level=0
        self.leaflevel=0
        return self.checkutil(root,0)
def checkutil(self,root,level):
        if root==None:
            return True
        if root.left==None and root.right==None:
            if self.leaflevel==0:
                self.leaflevel=level
                return True
            return level==self.leaflevel
        return (self.checkutil(root.left,level+1)and self.checkutil(root.right,level+1))   
        