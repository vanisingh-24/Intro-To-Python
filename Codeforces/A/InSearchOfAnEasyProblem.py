'''
https://codeforces.com/problemset/problem/1030/A
Solution: Straightforward. Run through the answers and return HARD at the first occurrence of a 1. Default return EASY.
'''

n = int(input())
s = input().split(' ')
 
if s.__contains__('1'):
  print('HARD')
else:
  print('EASY')