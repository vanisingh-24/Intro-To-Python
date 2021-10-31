'''
http://codeforces.com/problemset/problem/112/A
Solution: Run a loop over any string's length (since they are said to have same length)
Convert each letter of both string to same case and compare. Return -1 and 1 accordingly.
If complete strings match, 0 is returned.
'''

str1 = input().lower()
str2 = input().lower()
 
if str1 < str2:
    print(-1)
elif str1 > str2:
    print(1)
else:
    print(0)