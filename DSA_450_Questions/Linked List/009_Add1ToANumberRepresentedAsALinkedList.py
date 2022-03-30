## A number N is represented in Linked List such that each digit corresponds to a node in linked list. You need to add 1 to it.

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
