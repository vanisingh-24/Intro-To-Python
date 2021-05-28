#  Given a string in python, count number of numeric characters in the string and remove them from the string and print the string

string ='123geeks456for789geeks'
count = 0

newString = ""

for a in string:
  if(a.isnumeric()) == True:
    count += 1
  else:
    newString += a
print(count)
print(newString)