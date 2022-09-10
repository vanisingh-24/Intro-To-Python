## Given two numbers represented by two linked lists of size N and M. The task is to return a sum list.

def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            # new digit val
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)  # as in one place we have to put a single digit
            
            # update pointers
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy.next

# OR

def addTwoLists(self, first, second):
        nums1, nums2 = 0, 0
        
        while first:
            nums1 = nums1 * 10 + first.data
            first = first.next
        while second:
            nums2 = nums2 * 10 + second.data
            second = second.next
        sum = nums1 + nums2
        curr = head = Node(0)
        if sum == 0:
            return head
        while sum > 0:
            head.next = Node(sum % 10)
            head = head.next
            sum //= 10
            
        prev = None
        head = curr.next
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev
    
# OR

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Solution:
    def reverse(self, head):
        curr = head
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
        
    def addTwoLists(self, first, second):
        dummy = Node(None)
        curr = dummy
        carry = 0
        first = self.reverse(first)
        second = self.reverse(second)
        while first or second or carry == 1:
            sum = 0
            if first:
                sum += first.data
                first = first.next
            if second:
                sum += second.data
                second = second.next
            sum += carry
            carry = sum // 10
            newNode = Node(sum % 10)
            curr.next = newNode
            curr = curr.next
        ans = self.reverse(dummy.next)
        return ans
        