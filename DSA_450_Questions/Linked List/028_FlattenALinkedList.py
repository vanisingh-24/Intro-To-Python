## Given a Linked List of size N, where every node represents a sub-linked-list and contains two pointers:
## (i) a next pointer to the next node,
## (ii) a bottom pointer to a linked list where this node is head.
## Each of the sub-linked-list is in sorted order.
## Flatten the Link List such that all the nodes appear in a single level while maintaining the sorted order.

# Approach: Merge process

def flatten(root):
    if(root==None or root.next==None):
        return root
   
    root = mergeTwoLists(root,flatten(root.next))
   
    return root
    
def mergeTwoLists(a,b):
    if a == None:
        return b
    if b == None:
        return a
        
    result = None
    
    if(a.data<b.data):
        result = a
        result.bottom = mergeTwoLists(a.bottom, b)
    else:
        result = b
        result.bottom = mergeTwoLists(a, b.bottom)
   
    result.next = None
    return result

# OR

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None

def flatten(root):
    if(root==None or root.next==None):
        return root
   
    root = mergeTwoLists(root,flatten(root.next))
   
    return root
    
def mergeTwoLists(a,b):
    temp = Node(0)
    res=temp
   
    while(a!=None and b!=None):
        if(a.data<b.data):
            temp.bottom = a
            a = a.bottom
            temp=temp.bottom
        else:
            temp.bottom = b
            temp = temp.bottom
            b = b.bottom
   
    temp.bottom = a if(a!=None) else b
    return res.bottom
