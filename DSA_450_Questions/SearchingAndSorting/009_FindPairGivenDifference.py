## Given an array Arr[] of size L and a number N, you need to write a program to find if there exists a pair of elements in the array whose difference is N.

# Approach 1: Using dictionaries

class Solution:

    def findPair(self, arr, L,N):
        mpp = {}
        
        for i in range(L):
            if arr[i] in mpp.keys():
                mpp[arr[i]] += 1
            else:
                mpp[arr[i]] = 1
 
        for i in range(L):
            if N + arr[i] in mpp.keys() and N != 0:
                return True
     
        return False

# Approach 2: Two Pointer Approach

class Solution:

    def findPair(self, arr, L,N):
        arr.sort()
        l = 0 
        h = 1
        
        while l< len(arr) and h < len(arr):
            if arr[h] - arr[l] == N and h !=l: 
                return True
            elif arr[h] - arr[l] > N:
                l +=1
            else:
                h +=1
        return False