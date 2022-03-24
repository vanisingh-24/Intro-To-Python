## Given an unsorted array Arr of size N of positive integers.
## One number 'A' from set {1, 2, …N} is missing and one number 'B' occurs twice in array. Find these two numbers.

# Dictionaries
# j - repeating
# k - missing

class Solution:
    def findTwoElement( self,arr, n):
        arr.sort()
        d={}
        k=1
        for i in range(n):
            if arr[i] not in d:
                d[arr[i]]=1
            else:
                d[arr[i]]+=1
        for j in d:
            if d[j]>1:
                break
        for m in range(n):
            if arr[m]==k:
                k+=1
        return j,k