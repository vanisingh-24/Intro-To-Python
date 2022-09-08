## Given two singly linked lists of size N and M, write a program to get the point where two linked lists intersect each other.

# Two Pinter Solution

def intersetPoint(head1,head2):
    firstlist, secondlist = head1, head2 
    
    while firstlist != secondlist:
        firstlist = firstlist.next if firstlist else head2
        secondlist = secondlist.next if secondlist else head1
       
    return secondlist.data

# Hashing

def intersetPoint(head1,head2):
    s = set()
    
    while head1:
        s.add(head1)
        head1 = head1.next
        
    while head2:
        if head2 in s:
            return head2.data
        head2 = head2.next
    return None
