## Given a N x N matrix, where every row and column is sorted in non-decreasing order. Find the kth smallest element in the matrix.

# Simple Solution

def kthSmallest(mat, n, k):
    A=[]
    for i in mat:
        for j in i:
            A.append(j)
    A=sorted(A)
    return (A[k-1])

# Binary Search

def kthSmallest(mat, n, k):
    left, right = mat[0][0], mat[n-1][n-1]
            
    while left < right:
        mid = left + (right - left)//2
        
        total = 0
        
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] <= mid:
                    total+=1 
        
        if total < k:
            left = mid + 1
        else:
            right = mid
    return left