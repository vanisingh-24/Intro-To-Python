'''
https://codeforces.com/problemset/problem/50/A
Solution: Simply divide the board-area by tile-area. Do integer division to ignore the fractional tiles. 
'''

m,n = map(int, input().split())
print(m*n//2*1)