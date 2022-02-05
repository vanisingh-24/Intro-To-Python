## Find k’th smallest element in an array

# Naive solution

def kthSmallest(arr,k):
    arr.sort()
    return arr[k - 1]

arr = list(map(int, input().split(' ')))
k = int(input())
kthSmallest(arr,k)

