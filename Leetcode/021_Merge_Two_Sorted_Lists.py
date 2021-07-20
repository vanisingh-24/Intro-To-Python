# Merge two sorted linked lists and return it as a sorted list. 
# The list should be made by splicing together the nodes of the first two lists.

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy
        
        # both l1 and l2 not empty
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
            
        # If one list is empty and other is non empty
        if l1:              #l1 not null
            tail.next = l1
        elif l2:            #l2 not null
            tail.next = l2
            
        return dummy.next