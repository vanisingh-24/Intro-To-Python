## Find the largest rectangular area possible in a given histogram where the largest rectangle can be made of a number of contiguous bars.

def getMaxArea(self,histogram):
    stack = []
    max_area = 0 
    index = 0
    while index < len(histogram):
        if (not stack) or (histogram[stack[-1]] <= histogram[index]):
            stack.append(index)
            index += 1
        else:
            top_of_stack = stack.pop()
 
            area = (histogram[top_of_stack] * ((index - stack[-1] - 1) if stack else index))
            max_area = max(max_area, area)
 
    while stack:
        top_of_stack = stack.pop()
 
        area = (histogram[top_of_stack] * ((index - stack[-1] - 1) if stack else index))
        max_area = max(max_area, area)
 
    return max_area

# OR

def maxHist(heights):
  stack = []
  max_area = 0

  for i, h in enumerate(heights):
    start = i
    while stack and stack[-1][1] > h:
      index, height = stack.pop()
      max_area = max(max_area, height * (i - index))
      start = index
    stack.append((start,h))
  for i, h in stack:
    max_area = max(max_area, (len(heights) - i))
  return max_area

heights = [6,2,5,4,5,1,6]
maxHist(heights)