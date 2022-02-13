## Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# sort by start value

class Solution:
	def overlappedInterval(self, Intervals):
		Intervals.sort(key = lambda i: i[0])
		output = [Intervals[0]]
		
		for start, end in Intervals[1:]:
		    lastEnd = output[-1][1]
		    if start <= lastEnd:
		        output[-1][1] = max(lastEnd, end)
		    else:
		        output.append([start, end])
		        
		return output

# OR

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        output = [intervals[0]]
        
        for start, end in intervals[1:]:
            if start > output[-1][1]:
                output.append([start, end])
            elif end > output[-1][1]:
                output[-1][1] = end
        return output