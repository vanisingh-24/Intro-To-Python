## A number N is represented in Linked List such that each digit corresponds to a node in linked list. You need to add 1 to it.

# Simple Solution

def addOne(self, head):
        curr=head
        s=""
        while head!=None:
            s=s+str(head.data)
            head=head.next
        return Node(str(int(s)+1))
    
# OR

def addOne(self,head):
        def reverse(head):
            prev = None
        # reverse the elinked list
            while head:
                cur = head
                head= head.next
                cur.next=prev
                prev = cur
            
            return prev
            
        cur = dummy = reverse(head)
        
        
        carry =1
        
        while cur:
            cur.data+=carry
            carry = cur.data//10
            cur.data%=10
            prev = cur
            cur= cur.next
            
        if carry>0:
            prev.next = Node(carry)
        return reverse(dummy)
    
# OR

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def addOne(self,head):
        def reverse(head):
            prev=None
            curr=head
            while(curr):
                next=curr.next
                curr.next=prev
                prev=curr
                curr=next
            return prev
        head=reverse(head)
        carry=0
        curr=head
        prev=None
        curr.data+=1
        while(curr):
            sum=carry+curr.data
            carry=sum//10
            curr.data=sum%10
            prev=curr
            curr=curr.next
        if carry==1:
            prev.next=Node(carry)
        head=reverse(head)
        return head
