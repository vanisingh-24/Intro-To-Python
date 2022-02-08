## Write a program to cyclically rotate an array by one

# Reversal algorithm

def rotate(arr, n):
  i = 0
  j = n - 1
  while i != j:
    arr[i], arr[j] = arr[j] , arr[i]
    i += 1
  return arr

arr = [1,2,3,4,5]
n = len(arr)
rotate(arr, n)