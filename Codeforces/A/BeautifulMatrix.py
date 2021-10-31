'''
https://codeforces.com/problemset/problem/263/A
Solution: Idea is to find the cell containing 1 and then find the Manhattan distance from the center of the grid (that
would be 2,2 cell).
'''

for r in range(5):
    row = input().split(' ')
    if '1' in row:
        print(abs(2 - r) + abs(2 - row.index('1')))