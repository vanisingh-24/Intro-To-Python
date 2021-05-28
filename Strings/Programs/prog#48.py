# String slicing in Python to check if a string can become empty by recursive deletion

def checkEmpty(input, pattern):
  # If both are empty
  if len(input)==0 and len(pattern)==0:
    return 'true'

  # If only pattern is empty
  if len(pattern)==0:
    return 'true'
  
  while(len(input)!=0):

    # Find substring in main string
    index = input.find(pattern)

    # Check if substring is founded or not
    if (index == -1):
      return 'false'

    # slice input string into two parts
    input = input[0:index] + input[index + len(pattern):]

  return 'true'

# Driver Code
input ='GEEGEEKSKS'
pattern ='GEEKS'
print (checkEmpty(input, pattern))