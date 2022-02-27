## Given a row wise sorted matrix of size RxC where R and C are always odd, find the median of the matrix.

# Naive Solution

def median(self, matrix, r, c):
    b=[]
    for i in matrix:
        for j in i:
            b.append(j)
    b.sort()
    c=len(b)
    return b[c//2]

# OR

class Solution:
    def median(self, matrix, r, c):
        arr=[]
        for i in range(r):
            for j in range(c):
                arr.append(matrix[i][j])
        n=r*c
        arr=sorted(arr)
        return arr[(n//2)]

# Binary Search

class Solution:
    def median(self, matrix, r, c):
        left = 1
        right = 2000
        target = (r*c+1)//2
        while(left<right):
            mid = left + (right-left)//2
            count = 0
            for i in range(r):
                count += self.count(matrix[i],mid+1)
                
            if count < target:
                left = mid+1
            else:
                right = mid
                
        return left
        
    def count(self,arr,ele):
        left = 0
        right = len(arr)
        while(left<right):
            mid = left + (right-left)//2
            if arr[mid] < ele:
                left = mid+1
            else:
                right = mid
                
        return left

