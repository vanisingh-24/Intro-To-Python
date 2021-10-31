'''
http://codeforces.com/problemset/problem/59/A
Solution: Count the number of upper case letters.
Check for length of string to be odd or even and accordingly check if the string
of upper case or not. If so, convert the string to upper case. Else, convert to lowercase.
'''

s = input()
 
l = len(s)
count = 0
 
for i in s:
  if i >= 'A' and i <= 'Z':
    count = count + 1
 
if count > l/2:
  print(s.upper())
else:
  print(s.lower())