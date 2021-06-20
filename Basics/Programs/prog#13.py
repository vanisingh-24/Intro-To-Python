## Python program to find sum of series with cubes of first n natural numbers

def sumOfCubes(n):
  sum = 0
  for i in range(1,n+1):
    sum += i*i*i

  return sum

# Driver Code
n= 5
print(sumOfCubes(n))

# OR

def sumOfCubes(n):
  x = (n*(n+1)/2) ** 2
  return int(x)

n = 5
print(sumOfCubes(5))

