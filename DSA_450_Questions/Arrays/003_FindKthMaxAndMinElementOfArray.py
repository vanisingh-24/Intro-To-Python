## Find k’th smallest element in an array

# Naive solution

def kthSmallest(arr,k):
    arr.sort()
    return arr[k - 1]

arr = list(map(int, input().split(' ')))
k = int(input())
kthSmallest(arr,k)

# Quick Select Algorithm

def kthSmallest(arr, k):
        kth = len(arr) - k
        
        def quickSelect(l, r):
            pivot, p = arr[r], l
            for i in range(l, r):
                if arr[i] <= pivot:
                    arr[p], arr[i] = arr[i], arr[p]
                    p += 1
            arr[p], arr[r] = arr[r], arr[p]
            
            if p > k:
                return quickSelect(l, p - 1)
            elif p < k:
                return quickSelect(p + 1, r)
            else:
                return arr[p]
        
        return quickSelect(0, len(arr) - 1)

arr = list(map(int, input().split(' ')))
k = int(input())
kthSmallest(arr,k)