## Python Program for How to check if a given number is Fibonacci number

import math

def isPerfectSquare(x):
  s = int(math.sqrt(x))
  return s*s == x

def isFibonacci(n):
  return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)

for i in range(1,11):
  if(isFibonacci(i) == True):
    print(i, "is a fibonacci number")
  else:
    print(i, "is not a fibonaci number")
