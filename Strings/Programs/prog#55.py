# Convert a list of characters into a string

# Traversing a list
def convert(s):
  new = ""

  for x in s:
    new +=x

  return new

# Driver Code
s = ['g', 'e', 'e', 'k', 's', 'f', 'o', 'r', 'g', 'e', 'e', 'k', 's']
print(convert(s))

# OR
# Using join() function

def convert(s):
  str = ""

  return(str.join(s))

# Driver Code
s = ['g', 'e', 'e', 'k', 's', 'f', 'o', 'r', 'g', 'e', 'e', 'k', 's']
print(convert(s))