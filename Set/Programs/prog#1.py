# Ms. Gabriel Williams is a botany professor at District College. 
# One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.

def average(heights):
  heights = set(heights)
  return sum(heights)/len(heights)

# Driver Code
n = int(input())
arr = list(map(int, input().split()))
result = average(arr)
print(result)


