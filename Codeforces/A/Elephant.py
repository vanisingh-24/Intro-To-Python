'''
https://codeforces.com/problemset/problem/617/A
Solution: Keep the possible steps in decreasing order so that when we use them, we always try to use the larger step 
first, thereby minimizing the steps needed. Now iterate till n is positive and use the possible steps to decrement n.
Return the count of steps in the end. 
'''

n = int(input())
 
s = n//5
if (n % 5 == 0):
  print(s)
else:
  print(s+1)