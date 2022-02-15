## Given an unsorted array Arr of N positive and negative numbers. 
## Your task is to create an array of alternate positive and negative numbers without changing the relative order of positive and negative numbers.

class Solution:
    def rearrange(self,arr, n):
        t1 = []
        t2 = []
        ans = []
        for i in arr:
            if i > -1:
                t1.append(i)
            else:
                t2.append(i)
        
        i = j = k = 0
        while i < n:
            if j < len(t1):
                arr[i] = t1[j]
                j+=1
                i+=1
            if k < len(t2):
                arr[i] = t2[k]
                k+=1
                i+=1
                
        return arr