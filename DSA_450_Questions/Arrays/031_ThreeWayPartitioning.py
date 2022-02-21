## Given an array of size n and a range [a, b].
## The task is to partition the array around the range such that array is divided into three parts.
## 1) All elements smaller than a come first.
## 2) All elements in range a to b come next.
## 3) All elements greater than b appear in the end.

# Efficient Solution (3 Way QuickSort)

def threeWayPartition(array, a, b):
	    start = 0
        end = n - 1
        i = 0
  
        while i <= end:
            if array[i] < a:
                temp = array[i]
                array[i] = array[start]
                array[start] = temp
                i += 1
                start += 1
            elif array[i] > b:
                temp = array[i]
                array[i] = array[end]
                array[end] = temp
                end -= 1
            else:
                i += 1
                
        return array
