## Given a dictionary in Python, write a Python program to find the sum of all Items in the dictionary.

# 1. Using inbuilt sum function
def sum(dict):
  sum = 0
  for i in dict:
    sum = sum + dict[i]
  return sum

# Driver Code
dict = {'a': 100, 'b':200, 'c':300}
print(sum(dict))

# 2. Using For loop to iterate through values using values() function
def sum(dict):
  sum = 0
  for i in dict.values():
    sum = sum + i
  return sum

# Driver Function
dict = {'a': 100, 'b':200, 'c':300}
print("Sum :", sum(dict))
