'''
http://codeforces.com/problemset/problem/231/A
Solution: The idea is to parse each line of inputs (strings of 0 and 1) and take a count of 1s in it.
It can be done using Counter from collections package. If its >=2, then its a majority in 3 friends. 
Bingo => consider the current problem as solvable. Repeat this for all inputs.
'''

n = int(input())
count = 0
for i in range(0,n):
    x = input()
    if x.count('1') >= 2:
        count +=1
print(count)