# Given an array A containing n integers. 
# The task is to check whether the array is Monotonic or not. 
# An array is monotonic if it is either monotone increasing or monotone decreasing.

def isMonotonic(A):

	return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
			(all(A[i] >= A[i + 1] for i in range(len(A) - 1))

# Driver program
A = [6, 5, 4, 4]

print(isMonotonic(A))
