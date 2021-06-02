# Given a pair of non empty strings
# Count the number of matching characters in those strings.

def count(str1, str2):
  c,j = 0,0

  for i in str1:
    if str2.find(i)>=0 and j == str1.find(i):
      c += 1
    j += 1
  print('No. of characters are:', c)

def main():
  str1 = 'aabcddekll12@'
  str2 = 'bb2211@55k'
  count(str1, str2)

# Driver Code
if __name__ =="__main__":
  main()
