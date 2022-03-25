## You are given an array arr[] of size n. Find the total count of sub-arrays having their sum equal to 0.

# Approach 1: Using hashmap

def findSubArrays(arr,n):
    d = {}
    s = 0
    c = 0
    d[0] = 1
    for i in range(0, n):
        s = s + arr[i]
        if s in d:
            c += d[s]
                
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    return c


