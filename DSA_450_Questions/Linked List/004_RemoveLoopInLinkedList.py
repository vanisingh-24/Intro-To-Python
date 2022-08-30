## Given a linked list of N nodes such that it may contain a loop.
## Remove the loop from the linked list, if it is present.  

# Approach 1: Using hashing

class Solution:
    def removeLoop(self, head):
        s = set()
        while head != None:
            if head.next not in s:
                s.add(head)
                head = head.next
            else:
                head.next = None

# Approach 2: Simple Approach

class Solution:
    def removeLoop(self, head):
        n = len(head)
        ptr = head
        i=0
        while i<=n:
            if ptr.next==None:
                return 1
            if i==n-1 and ptr.next!=None:
                ptr.next=None
                return 1
            ptr=ptr.next
            i+=1

# Approach 3: Floyd's Cycle Algorithm

class Solution:
    def removeLoop(self, head):
        slow, fast = head, head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if slow == fast:
                slow = head
                if slow == fast:
                    while fast.next != slow:
                        fast = fast.next
                else:
                    while slow.next != fast.next:
                        slow = slow.next
                        fast = fast.next
                fast.next = None