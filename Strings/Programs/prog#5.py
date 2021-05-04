# the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string.
# String traversal will take place from left to right, not from right to left.

def count_substring(string, sub_string):
  c = 0
  l = len(sub_string)
  for i in range(0,len(string)):
    s = string[i:i+l]
    if s==sub_string:
      c+=1
  return c

string = input().strip()
sub_string = input().strip()
    
count = count_substring(string, sub_string)
print(count)

## OR
# using string.find() method
# SYNTAX - string.find(substring, startIndex, endIndex)

def count_substring(string, sub_string):

    c = 0
    x = -1
    while(x<len(string)):
        z = string.find(sub_string, x+1)
        if z == -1:
            break
        c+=1
        x = z
    return c

string = input().strip()
sub_string = input().strip()
    
count = count_substring(string, sub_string)
print(count)