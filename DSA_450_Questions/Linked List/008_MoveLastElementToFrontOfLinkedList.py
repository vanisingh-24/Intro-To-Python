## Write a function that moves the last element to the front in a given Singly Linked List.

# Simple Approach

def moveToFront(head):
    temp = head
    secondLast = None
    while temp and temp.next:
        secondLast = temp
        temp = temp.next
    secondLast.next = None
    temp.next = head
    head = temp
    return head


