## You are given N number of books. Every ith book has Ai number of pages.
## You have to allocate contiguous books to M number of students.

# Binary Search 

class Solution:
    def is_possible(self, A, N, M, mid):
        num_student = 1 
        pages = 0
        for i in range(N):
            if A[i] > mid:
                return False
            if (A[i] + pages) > mid:
                num_student += 1
                pages = A[i]
            else:
                pages += A[i]
        if num_student > M:
            return False
        return True
    
    def findPages(self,A, N, M):
        if N < M:
            return -1
        if N == M:
            return max(A)
        low = max(A)  
        high = sum(A) 
        res = -1
        while low <= high:
            mid = (low+high) // 2
            if self.is_possible(A, N, M, mid):
                res = mid
                high = mid - 1
            else:
                low = mid +1
        return res