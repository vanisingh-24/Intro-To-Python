'''
http://codeforces.com/problemset/problem/281/A
Nothing special. Just check the first character. If its in lowercase, print its upper case and
rest of the string as it is. Otherwise, print the original string as it is.
'''

s = input()
print(s[0].upper() + s[1:])