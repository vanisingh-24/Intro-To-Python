## Given two sorted arrays array1 and array2 of size m and n respectively.
## Find the median of the two sorted arrays.

# Binary Search

def findMedianSortedArray(nums1, nums2):
  A, B = nums1, nums2
  total = len(nums1) + len(nums2)
  half = total // 2

  if len(B) < len(A):
    A, B = B, A

  l, r = 0, len(A)-1
  while True:
    i = (l + r) // 2
    j = half - i - 2

    ALeft = A[i] if i >= 0 else float("-infinity")
    ARight = A[i+1] if i+1 < len(A) else float("infinity")
    BLeft = B[j] if j >= 0 else float("-infinity")
    BRight = B[j+1] if j+1 < len(B) else float("infinity")

    if ALeft <= BRight and BLeft <= ARight:
      if total % 2:
        return min(ARight, BRight)
      return max(ALeft, BLeft) + min(ARight, BRight) / 2
    elif ALeft > BRight:
      r = i-1
    else:
      l = i+1

nums1 = [1,2,3,4,5,6,7,8]
nums2 = [1,2,3,4,5]
findMedianSortedArray(nums1, nums2)

# Simple Solution

def MedianOfArrays(self, array1, array2):
        #code here
        a=array1+array2
        a.sort()
        if len(a)%2==0:
            p=int(len(a)/2)
            m=(a[p]+a[p-1])/2
            if m%2==0.0 or m%2==1.0:
                return int(m)
            else:
                return m
        else:
            p=int(len(a)/2)
            return a[p]