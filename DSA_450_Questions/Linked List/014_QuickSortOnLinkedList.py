## Sort the given Linked List using quicksort. which takes O(n^2) time in worst case and O(nLogn) in average and best cases, otherwise you may get TLE.

def quickSort(head):
    #return head after sorting
    if not head or not head.next:
        return head
    pivot = head

    smallhead = small = Node(-1)
    largehead = large = Node(-1)
    curr = head.next
    while curr:
        if curr == pivot:
            curr = curr.next
        elif curr.data < pivot.data:
            small.next = curr
            curr = curr.next
            small = small.next
        else:
            large.next = curr
            curr = curr.next
            large = large.next
    
    small.next = None
    large.next = None
    
    small = quickSort(smallhead.next)
    pivot.next = None
    large = quickSort(largehead.next)
    
    temp = small
    while temp and temp.next:
        temp = temp.next
    if temp:
        temp.next = pivot
    else:
        small = pivot
    pivot.next = large
    return small

