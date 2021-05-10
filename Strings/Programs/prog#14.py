# Python program to check if a substring is present in a given string

# Using user defined function find()

def check(string, sub_str):
  if (string.find(sub_str) == -1):
    print("No")
  else:
    print("Yes")

string="geeks for geeks"
sub_str = "geek"
check(string,sub_str)




