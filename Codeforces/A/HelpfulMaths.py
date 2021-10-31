'''
https://codeforces.com/problemset/problem/339/A
Solution: Split the expression by +. Sort the resulting list and return the list joined by +. Also take care of inputs
with +, which should be returned as is. 
'''

print("+".join(sorted(c for c in input() if c != '+')))