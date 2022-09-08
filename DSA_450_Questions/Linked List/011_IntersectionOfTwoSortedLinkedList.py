## Given two lists sorted in increasing order, create a new list representing the intersection of the two lists.

# Using dummy node

def findIntersection(head1,head2):
    prev = None
    dummy = Node(0)
    curr = dummy
    while head1 and head2:
        if head1.data == head2.data:
            curr.next = Node(head1.data)
            curr = curr.next
            head1 = head1.next
            head2 = head2.next
        elif head1.data > head2.data:
            head2 = head2.next
        else:
            head1 = head1.next
    
    return dummy.next 

# Using recursion

def findIntersection(head1,head2):
    if head1 == None or head2 == None:
        return None
 
    if head1.data < head2.data:
        return findIntersection(head1.next, head2)
 
    if head1.data > head2.data:
        return findIntersection(head1, head2.next)
 
    temp = Node(0)
    temp.data = head1.data
 
    temp.next = findIntersection(head1.next, head2.next)
    return temp