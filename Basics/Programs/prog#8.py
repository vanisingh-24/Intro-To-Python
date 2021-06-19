# Python Program for n-th Fibonacci number

def fib(n):
  if(n<=0):
    print('Incorrect Input')
  elif(n==1):
    return 0
  elif(n==2):
    return 1
  else:
    return(fib(n-1)+fib(n-1))

print(fib(9))

