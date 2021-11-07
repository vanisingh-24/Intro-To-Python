'''
https://codeforces.com/problemset/problem/228/A
Solution: We want to find the unique colors of the horse shoes present, and that should be subtracted from 4 (for four
legs of the horse). That is number of colors we need to have distinctly colored horse shoes.
'''

n = input().split(' ')
s = set(n)
 
print(4 - len(s))