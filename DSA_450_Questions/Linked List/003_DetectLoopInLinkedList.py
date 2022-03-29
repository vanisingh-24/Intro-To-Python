## Given a linked list of N nodes. The task is to check if the linked list has a loop. Linked list can contain self loop.

# Approach 1: Floyd's Cycle Algorithm

class Solution:
    def detectLoop(self, head):
        low = head
        high = head
        while low and high and high.next:
            low = low.next
            high = high.next.next
            if low == high:
                return True
        return False

# Approach 2: Hashing Approach

class Solution:
    def detectLoop(self, head):
        s = set()
        temp = head
        while temp:
            if temp in s:
                return True
            s.add(temp)
            temp = temp.next
        return False
