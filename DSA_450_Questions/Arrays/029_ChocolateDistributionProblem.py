## Given an array of n integers where each value represents the number of chocolates in a packet.
## Each packet can have a variable number of chocolates. 
## There are m students, the task is to distribute chocolate packets such that: 
## 1. Each student gets one packet.
## 2. The difference between the number of chocolates in the packet with maximum chocolates and packet with minimum chocolates given to the students is minimum.

# Simple solution

def findMinDiff(arr, n, m):
    if (m==0 or n==0):
        return 0
  
    arr.sort()
  
    if (n < m):
        return -1
  
    min_diff = arr[n-1] - arr[0]
    for i in range(len(arr) - m + 1):
        min_diff = min(min_diff ,  arr[i + m - 1] - arr[i])
      
    return min_diff

