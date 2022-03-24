## Given an array A of N elements. Find the majority element in the array.

# Approach 1: Brute Force Approach

class Solution:
    def majorityElement(self, A, N):
        maxCount = 0
        index = -1  
        for i in range(N):
            count = 0
            for j in range(N):
                if(A[i] == A[j]):
                    count += 1

            if(count > maxCount):
                maxCount = count
                index = i
        if (maxCount > N//2):
            return (A[index])
        else:
            return -1

# Approach 2: Using Hashmap

class Solution:
    def majorityElement(self, A, N):
        dict ={}
       
        for num in A:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
       
        count = N//2 
       
        for num in A:
            value = dict[num]
            if value > count:
                return num
        return -1