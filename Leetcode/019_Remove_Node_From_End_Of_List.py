# Given the head of a linked list, remove the nth node from the end of the list and return its head.

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        left = right = head
        for i in range(n):
            right = right.next
            
        if right is None:
            return head.next
        
        while right.next:
            right = right.next
            left = left.next
        left.next = left.next.next
        return head