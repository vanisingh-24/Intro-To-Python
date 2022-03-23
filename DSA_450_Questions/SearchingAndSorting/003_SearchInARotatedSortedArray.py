## Given a sorted and rotated array A of N distinct elements which is rotated at some point, and given an element key.
## The task is to find the index of the given element key in the array A.

class Solution:
    def search(self, A : list, l : int, h : int, key : int):
        while l <= h:
            mid = l + (h-l) // 2
            if A[mid] == key:
                return mid
            elif A[mid] >= A[l]:
                if key >= A[l] and key <= A[mid]:
                    h = mid-1
                else:
                    l = mid+1
            else:
                if key > A[mid] and key <= A[h]:
                    l = mid+1
                else:
                    h = mid-1
        return -1