'''
https://codeforces.com/problemset/problem/520/A
Solution: Maintain a set of characters seen in the string. In the end, the size of that set should be 26 denoting all
characters were observed at least once in the string. Make sure we add characters in one case in the set to deal with
upper/lower case characters.  
'''

n = int(input())
string = input()

s = set()

for i in range(n):
  s.add(string[i].lower())

if len(s) == 26:
  print('YES')
else:
  print('NO')