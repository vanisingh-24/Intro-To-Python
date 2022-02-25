## Given a boolean 2D array of n x m dimensions where each row is sorted.
## Find the 0-based index of the first row that has the maximum number of 1's.

# Brute Force Approach

def rowWithMax1s(self,arr, n, m):
	    Max=0
        temp=0
        for i in range(n):
            count=0
            if(arr[i].count(1)>Max):
                Max=arr[i].count(1)
                temp=i
        if(Max==0):
            return -1
        return temp

# Binary Search Approach

def rowWithMax1s(self,arr, n, m):
           
    max=-1
    max_row_index=0
    for i in range(n):
        index=self.find(arr[i],0,m-1)
        if index!= -1 and m-index>max_row_index:
            max_row_index=m-index
            max=i
    return max
        
def find(self,arr,low,high):
    if low<=high:
        mid=(low+high)//2
        if (mid==0 or arr[mid-1]==0) and arr[mid]==1:
            return mid
        elif arr[mid]==0:
            return self.find(arr,mid+1,high)
        else:
            return self.find(arr,low,mid-1)
    return -1



