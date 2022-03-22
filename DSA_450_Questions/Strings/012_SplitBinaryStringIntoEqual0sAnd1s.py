## Given a binary string str of length N, the task is to find the maximum count of consecutive substrings str can be divided into such that all the substrings are balanced i.e. they have equal number of 0s and 1s.
## If it is not possible to split str satisfying the conditions then print -1.

# Brute Force Approach

def maxSub(str, n):
  count0 = 0
  count1 = 0
  count = 0

  for i in range(n):
    if str[i] == '0':
      count0 += 1
    else:
      count1 += 1

    if count0 == count1:
     count += 1

  if count0 != count1:
    return -1
  return count

str = "0100110101"
n = 10
maxSub(str, n)