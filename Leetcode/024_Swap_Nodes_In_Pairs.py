# Given a linked list, swap every two adjacent nodes and return its head.
# You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        
        
        while curr and curr.next:
            # save ptrs
            nxtPair = curr.next.next
            second = curr.next
            
            # reverse this pair
            second.next = curr
            curr.next = nxtPair
            prev.next = second
            
            # update ptrs
            prev = curr
            curr = nxtPair
            
        return dummy.next