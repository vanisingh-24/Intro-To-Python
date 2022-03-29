## Given a linked list of size N.
## The task is to reverse every k nodes (where k is an input to the function) in the linked list.
## If the number of nodes is not a multiple of k then left-out nodes, in the end, should be considered as a group and must be reversed

# Iterative Approach

class Solution:
    def reverse(self,head, k):
        if head is None:
            return None
            
        curr = head
        prev = None
        next = None
        i = 0
        while curr and i < k:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            i += 1
        head.next = self.reverse(curr, k)
        return prev

