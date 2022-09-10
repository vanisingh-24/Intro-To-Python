## Given head, the head of a singly linked list, find if the linked list is circular or not.
## A linked list is called circular if it not NULL terminated and all nodes are connected in the form of a cycle.
## An empty linked list is considered as circular.

def isCircular(head):
    temp = head
    while temp.next:
        if temp.next == head:
            return 1
        temp = temp.next
    return 0

# OR

def isCircular(head):
    slow = fast = head
        
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
        
# OR

def hasCycle(self, head):
        s = set()
        while head:
            if head in s:
                return True
            s.add(head)
            head = head.next
        return False
        