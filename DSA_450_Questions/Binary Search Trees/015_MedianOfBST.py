## Given a Binary Search Tree of size N, find the Median of its Node values.

def findMedian(root):
    l=[]
    def inorder(root, lis):
        if not root:
            return
        inorder(root.left, lis)
        lis.append(root.data)
        inorder(root.right, lis)
        
    inorder(root, l)
    mid = len(l)//2
    
    if len(l)%2 != 0:
        return l[mid]
    else:
        key=(l[mid]+l[mid-1])/2
        if int(key)==key:
            return int(key)
        else:
            return key