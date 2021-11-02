'''
http://codeforces.com/problemset/problem/110/A
Solution: Take number input as String. Build a digit-frequency map of it. Count the frequency
pf 4 and 7. If its either 4 or 7, print YES. Else, print NO.
'''

n = input()
count = 0
 
for i in range(len(n)):
  if n[i] == '4' or n[i] == '7':
    count += 1
 
if count == 4 or count == 7:
  print('YES')
else:
  print('NO')