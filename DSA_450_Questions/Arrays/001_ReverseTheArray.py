## Write a program to reverse an array or string

# Recursive python program to reverse an array

def reverseList(A, start, end):
	if start >= end:
		return
	A[start], A[end] = A[end], A[start]
	reverseList(A, start+1, end-1)

# Driver function
A = [1, 2, 3, 4, 5, 6]
reverseList(A, 0, 5)
print(A)

# Using Python List slicing

def reverseList(A):
  print( A[::-1])
     
# Driver function
A = [1, 2, 3, 4, 5, 6]
reverseList(A) 