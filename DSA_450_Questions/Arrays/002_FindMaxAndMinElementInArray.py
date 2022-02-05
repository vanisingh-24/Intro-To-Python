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

