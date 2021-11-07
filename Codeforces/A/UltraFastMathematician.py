'''
https://codeforces.com/problemset/problem/61/A
Solution: Brute force, where we compare each corresponding characters of both numbers, thereby adding 0 when same and
1 when different to the resultant string. 
'''

n1 = input()
n2 = input()
 
result = []
 
for i, x in enumerate(n1):
  if x == n2[i]:
    result.append('0')
  else:
    result.append('1')
 
print("".join(result))