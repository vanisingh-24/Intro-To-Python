'''
http://codeforces.com/problemset/problem/141/A
Solution: Create frequency distribution (lexically ordered) of each word. Add them to make
their joint distribution. Compare with the similar distribution of the jumbled words.
If they match, return YES. Else return NO.
'''

g = input().upper()
h = input().upper()
mixed = ''.join(sorted(input().upper()))

men = ''.join(sorted(g+h))

if men == mixed:
  print('YES')
else:
  print('NO')