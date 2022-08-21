## Given an array A[] of N integers and replace every element with the least greater element on its right side in the array
## If there are no greater elements on the right side, replace it with -1. 
 
# Using bisect module 

from typing import List
from bisect import insort,bisect

class Solution:
    def findLeastGreater(self, n : int, arr : List[int]) -> List[int]:
        res=[]
        ans=[]
        
        for i in range(n-1,-1,-1):
            insort(res,arr[i])
            x=bisect(res,arr[i])
            if x==len(res):
                ans.append(-1)
            else:
                ans.append(res[x])
        return ans[::-1] 

#  Alternate Method

from typing import List

class Node:
    def __init__(self, data):
        self.data=data
        self.left = self.right = None

class Solution:
    def __init__(self):
        self.succ=None
    
    def insert(self, root, data):
        if root is None:
            return Node(data)
        if data<root.data:
            self.succ = root
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        return root
    
    def findLeastGreater(self, n : int, arr : List[int]) -> List[int]:
        root=None
        for i in range(n-1, -1, -1):
            self.succ=None
            root = self.insert(root, arr[i])
            arr[i]=self.succ.data if self.succ else -1
        return arr