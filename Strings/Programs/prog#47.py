# Execute a String of Code in Python

def exec_code():
  code = """
def factorial(num):
  fact = 1
  for i in range(1, num+1):
    fact = fact*i
  return fact
print(factorial(5))
"""
  exec(code)

# Driver Code
exec_code()