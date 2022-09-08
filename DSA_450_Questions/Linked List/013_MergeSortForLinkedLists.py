## Given Pointer/Reference to the head of the linked list, the task is to Sort the given linked list using Merge Sort.

def getMid(self, head):
        if not head:
            return head
        slow =  head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow
        
def merge(self, left, right):
        tail = dummy = Node(0)
        
        while left and right:
            if left.data < right.data:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        if left:
            tail.next = left
        if right:
            tail.next = right
            
        return dummy.next
        
def mergeSort(self, head):
        if not head or not head.next:
            return head
            
        left = head
        right = self.getMid(head)
        temp = right.next 
        right.next = None
        right = temp
        
        left = self.mergeSort(left)
        right = self.mergeSort(right)
        return self.merge(left, right)
