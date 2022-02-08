## Largest Sum Contiguous Subarray

# Kadane's Algorithm

def maxSubArraySum(nums,N):
  partial_sum = nums[0]
  global_max = nums[0]
        
  for i in range(1, N):
    partial_sum = max(partial_sum + nums[i], nums[i])
    global_max = max(global_max, partial_sum)
  return global_max

nums = [-2, -3, 4, -1, -2, 1, 5, -3]
N = len(nums)
maxSubArraySum(nums, N)