# We are given two sets of sizes n and m respectively and we need to find the number of pairs that are complete on concatenating each string from set 1 to each string from set 2.

def completePair(set1, set2):

  count = 0
  for str1 in set1:
    for str2 in set2:
      result = str1+str2

      tempSet = set([ch for ch in result if (ord(ch)>=ord('a') and ord(ch)<=ord('z'))])
      if len(tempSet)==26:
        count = count+1
  print(count)

# Driver Code
set1 = ['abcdefgh', 'geeksforgeeks','lmnopqrst', 'abc']
set2 = ['ijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz','defghijklmnopqrstuvwxyz']
completePair(set1,set2)