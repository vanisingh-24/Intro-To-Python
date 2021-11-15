'''
https://codeforces.com/problemset/problem/443/A
Solution: Remove the braces, split by the separators and then add the list of characters to a set. The size of that 
set is the no of distinct characters observed. 
'''

res = set()
 
for i in input():
  if i in 'abcdefghijklmnopqrstuvwxyz':
    res.add(i)
 
print(len(res))