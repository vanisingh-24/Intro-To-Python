## Given an unsorted linked list of N nodes.
## The task is to remove duplicate elements from this unsorted Linked List.
## When a value appears in multiple nodes, the node which appeared first should be kept, all others duplicates are to be removed.

# Approach 1: Hashing

def removeDuplicates(self, head):
        h = set()
        curr = head
        h.add(head.data)
        while curr.next:
            if curr.next.data in h:
                curr.next = curr.next.next
            else:
                h.add(curr.next.data)
                curr = curr.next
        return head
    
# OR
class Solution:
    def removeDuplicates(self, head):
        if not head:
            return head
        s = set()
        curr = head
        prev = None
        while curr:
            val = curr.data
            if val in s:
                prev.next = curr.next
            else:
                s.add(val)
                prev = curr
            curr = curr.next
        return head


