## Given a singly linked list consisting of N nodes.
## The task is to remove duplicates (nodes with duplicate values) from the given list (if exists).

# Simple solution

def removeDuplicates(head):
    if not head:
        return

    curr = head
    while curr and curr.next:
        if curr.data == curr.next.data:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head

