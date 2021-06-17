# Given multiple numbers and a number n, the task is to print the remainder after multiply all the number divide by n.

def findRemainder(arr,len,n):
  mul = 1

  for i in arr:
    mul = mul * (i%n)

  return mul%n

arr = [100, 10, 5, 25, 35, 14]
len = len(arr)
n = 11
print(findRemainder(arr,len,n))

