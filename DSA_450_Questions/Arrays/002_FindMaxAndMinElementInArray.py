## Find the minimum and maximum element in an array

# Naive solution

def getMaxMin(nums):
  max = min = nums[0]

  for i in range(1, len(nums)):
    if nums[i] > max:
      max = nums[i]
    elif nums[i] < min:
      min = nums[i]

  print(min, end=" ")
  print(max)

if __name__ == '__main__':
  nums = [24, 3, 45, 121, 29]
  getMaxMin(nums)

# Optimized solution to find the minimum and maximum number in a list by considering the elements in pairs.

def getMaxMin(nums):
  n = len(nums)

  if(n%2 == 0):
    maximum = max(nums[0], nums[1])
    minimum = min(nums[0], nums[1])
    i = 2
  else:
    maximum = minimum = nums[0]
    i = 1

  while i < n-1:
    if nums[i] < nums[i+1]:
      maximum = max(maximum, nums[i+1])
      minimum = min(minimum, nums[i])
    else:
      maximum = max(maximum, nums[i])
      minimum = min(minimum, nums[i+1])
    i += 2

  return (maximum, minimum)

if __name__ =='__main__':
	
	arr = [9, 1, 45, 2, 330, 3]
	maximum, minimum = getMaxMin(arr)
	print("Minimum element is", minimum)
	print("Maximum element is", maximum)