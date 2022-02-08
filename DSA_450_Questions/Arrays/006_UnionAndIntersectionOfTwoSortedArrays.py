## Find the union and intersection of two sorted arrays

# union

def union(arr1, arr2, m, n):
  i = 0
  j = 0
  while i < m and j < n:
    if arr1[i] < arr2[j]:
      print(arr1[i], end=" ")
      i += 1
    elif arr1[i] > arr2[j]:
      print(arr2[j], end=" ")
      j += 1
    else:
      print(arr2[j], end=" ")
      i += 1
      j += 1

  while i < m:
    print(arr1[i])
    i += 1

  while j < n:
    print(arr2[j])
    j += 1

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
m = len(arr1)
n = len(arr2)
union(arr1, arr2, m, n)

# intersection

def intersection(arr1, arr2, m, n):
  i = 0
  j = 0
  while i < m and j < n:
    if arr1[i] < arr2[j]:
      i += 1
    elif arr1[i] > arr2[j]:
      j += 1
    else:
      print(arr1[i], end=" ")
      i += 1
      j += 1

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
m = len(arr1)
n = len(arr2)
intersection(arr1, arr2, m, n)