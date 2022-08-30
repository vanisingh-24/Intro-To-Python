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

# OR

def moveToFront(self, head):
        if head is None or head.next is None:
            return head
            
        prev = head
        curr = head.next
        while curr.next != None:
            prev = prev.next
            curr = curr.next
        prev.next = None
        curr.next = head
        head = curr
        return head
