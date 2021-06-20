## Python Program for Sum of squares of first n natural numbers

def sumOfSquares(n):
  sum = 0

  for i in range(1,n+1):
    sum = sum+(i*i)
  return sum

# Driver Code
n = 4
print(sumOfSquares(n))

# OR

def sumOfSquares(n):
  return (n*(n+1)*(2*n+1)) // 6

n = 4
print(sumOfSquares(n))


