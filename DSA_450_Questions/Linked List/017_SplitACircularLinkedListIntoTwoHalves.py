## Given a Cirular Linked List of size N, split it into two halves circular lists.
## If there are odd number of nodes in the given circular linked list then out of the resulting two halved lists, first list should have one node more than the second list.
## The resultant lists should also be circular lists and not linear lists.

# 

class Solution:
    def splitList(self, head, head1, head2):
        if not head:
            return None
            
        slow = fast = head
        while fast.next.next != head and fast.next != head:
            slow = slow.next
            fast = fast.next.next
            
        head1 = head
        head2 = slow.next
        slow.next = head
        
        curr = head2
        while curr.next != head:
            curr = curr.next
        curr.next = head2
        
        #this is to emulate pass by reference in python please don't delete below line.
        return head1,head2

