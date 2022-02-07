## Move all the negative elements to one side of the array

# Quick Sort

def rearrange(arr, n):
  j = 0

  for i in range(0, n):
    if arr[i] < 0:
      temp = arr[i]
      arr[i] = arr[j]
      arr[j] = temp
      j += 1
  return arr

arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
n = len(arr)
rearrange(arr, n)

# or

def Rearrange( a, n):
    # pivot = 0
    i = -1
    for j in range(0, n) :
        if (a[j] < 0) :
            i += 1
            a[i], a[j] = a[j], a[i]
    return a
    
a = [2, -4, 7,-3, 4]
n = len(a)
rearrange(a, n)