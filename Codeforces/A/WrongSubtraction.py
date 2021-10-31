'''
https://codeforces.com/problemset/problem/977/A
Solution: Simply perform the actions for zero/non-zero last digit of n for k times. Return the final value of n. 
'''

n, k =map(int, input().split(' '))
 
for i in range(1,k+1):
  if n % 10 == 0:
    n = n //10
  else:
    n = n -1
 
print(n)