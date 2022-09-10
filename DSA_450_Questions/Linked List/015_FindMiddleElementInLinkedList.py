## Given a singly linked list of N nodes.
## The task is to find the middle of the linked list.

# Floyds Cycle Algorithm

def findMid(self, head):
        if not head:
            return head
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow.data
    
# Brute Force

def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = dummy
        counter = 0
        while curr.next:
            counter += 1
            curr = curr.next
        counter2 = 0
        while dummy.next:
            if counter2 > counter//2:
                break
            counter2 += 1
            dummy = dummy.next
        return dummy