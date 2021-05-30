# Given the string, we have to remove the ith indexed character from the string.

def remove(string,i):

  a = string[: i]
  b = string[i+1: ]
  
  return a+b

# Driver Code
string = "geeksFORgeeks"
i = 5
print(remove(string,i))