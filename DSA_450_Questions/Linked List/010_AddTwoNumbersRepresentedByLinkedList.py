## Given two numbers represented by two linked lists of size N and M. The task is to return a sum list.

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
        