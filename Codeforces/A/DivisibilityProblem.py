'''
https://codeforces.com/problemset/problem/1328/A
Solution: Direct application of ceil of division. When a/b is evaluated, the quotient may be
a floating point. That means b does not completely divide a. For that, we need to round up
the quotient since we are only allowed addition of 1. Now the ceil factor of the division and
the b are multiplied to get the divisible multiple of a. We need to return the difference of 
this value and current a. 
We employ the ceil equivalent rather than using library function here. 
'''

n = int(input())
 
for i in range(n):
  a,b = map(int, input().split(' '))
  
  if a%b == 0:
    print('0')
  else:
    print(b - (a%b))