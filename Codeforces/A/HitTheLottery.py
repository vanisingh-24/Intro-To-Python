'''
https://codeforces.com/problemset/problem/996/A
Solution: This the popular coin change problem. We can use the standard quadratic DP solution, but since the coins
are less, we just iterate over them and compute the bills. Since we are minimizing the bills used, we go over the 
coins in decreasing order so that we use the higher dollar value bills to reduce their counts. 
'''

n = int(input())
bills = [100, 20, 10, 5, 1]
c = 0

for bill in bills:
      if (n >= bill) and (n % bill != n):
            c =c + (n // bill)
            n %= bill
print(c)