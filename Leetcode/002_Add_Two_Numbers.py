# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

class Solution:
    def addTwoNumbers(self, l1, l2):
        head = ListNode()
        temp = head
        carry = 0
        
        # Extract digits from l1 and l2
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
         
            # New Digit
            out = val1 + val2 + carry
            carry = out // 10
            out = out % 10
        
            temp.next = ListNode(out)
        
            # Update pointer
            temp = temp.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return head.next

# OR

class Solution:
    def addTwoNumbers(self, l1, l2):
        head = ListNode(0)
        temp = head
        carry = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # out = val1 + val2 + carry
            # carry = out / 10
            
            carry, out = divmod(val1 + val2 + carry, 10)
            
            temp.next = ListNode(out)
            temp = temp.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if(carry > 0):
            temp.next = ListNode(carry)
            
        return head.next
        
