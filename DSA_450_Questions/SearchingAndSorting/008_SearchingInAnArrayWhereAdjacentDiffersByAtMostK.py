## A step array is an array of integer where each element has a difference of at most k with its neighbor.
## Given a key x, we need to find the index value of x if multiple elements exist, return the first occurrence of the key.

# Approach1 1: Simple Approach

def search (arr, n, x, k) : 
    if x in arr:
        return arr.index(x)
    else:
        return -1

# Approach 2: Optimized Solution

def search (arr, n, x, k) : 
    i = 0
    while i < n:
        if arr[i] == x:
            return i
        i = i + max(1, int(abs(arr[i]-x)/k))
    return -1