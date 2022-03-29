##

# Approach 1: Iterative Approach

class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

# Approach 2: Recursive Approach

class Solution:
    def reverseList(self, head):
        if head is None:
            return head
        
        first = head
        rest = first.next
        
        if rest is None:
            return head
            
        rest = self.reverseList(rest)
        
        first.next.next = first
        first.next = None
        head = rest
        
        return head
