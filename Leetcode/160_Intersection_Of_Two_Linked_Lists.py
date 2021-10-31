# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p1 = headA
        p2 = headB
        
        while p1 != p2:
            if p1:
                p1 = p1.next
            else:
                p1 = headB
            if p2:
                p2 = p2.next
            else:
                p2 = headA
                
        return p1

# OR

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        currA, currB = headA, headB
        a,b = 0, 0
        
        while currA:
            a += 1
            currA = currA.next
        while currB:
            b += 1
            currB = currB.next
            
        if a > b:
            currLong = headA
            diff = a-b
            currShort = headB
        else:
            currLong = headB
            diff = b-a
            currShort = headA
            
        i = 0
        while i < diff:
            i += 1
            currLong = currLong.next
            
        while currLong != currShort:
            currLong = currLong.next
            currShort = currShort.next
            
        return currLong
