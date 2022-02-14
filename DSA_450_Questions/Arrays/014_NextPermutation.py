## Next Permutation

# approach1

def nextPermutation(nums):
  N = len(nums)
  pivot = 0
        
  # Find pivot
  for i in range(N-1, 0, -1):
    if nums[i-1] < nums[i]:
      pivot = i
      break
    if pivot == 0:
      nums.sort()
      return
        
  #Find swap which first no. > pivot
  swap = N-1
  while nums[pivot - 1] >= nums[swap]:
    swap -= 1
        
  # swap
  nums[swap], nums[pivot-1] = nums[pivot-1], nums[swap]
        
  # reverse from pivot
  nums[pivot:] = sorted(nums[pivot:])
 
# approach 2(optimized)

def nextPermutation(arr):
  n = len(arr)
  k = n-2
  while k >= 0:
    if arr[k] < arr[k+1]:
      break
    k -= 1

  if k < 0:
    arr = arr[::-1]
  else:
    for l in range(n-1, k, -1):
      if arr[l] > arr[k]:
        break
    arr[k], arr[l] = arr[l], arr[k]
    arr[k+1:] = reversed(arr[k+1:])
  return arr

arr = [5, 3, 4, 9, 7, 6]
print(nextPermutation(arr))

