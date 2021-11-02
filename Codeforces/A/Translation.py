'''
http://codeforces.com/problemset/problem/41/A
Solution: Base case checks if the lengths of the 2 strings does not equate. Otherwise, iterate
over either length and check from left and right of the 2 strings respectively for same character.
Return NO is it fails anywhere. Else, return YES after iteration.
'''

def solve(s, t):
  len1 = len(s)
  len2 = len(t)
 
  if(len1!=len2):
    return "NO"
 
  for i in range(0,len1):
    if(s[i]!=t[len1-i-1]):
      return "NO"
 
  return "YES"
 
if __name__ == "__main__":
  s = input()
  t = input()
  print(solve(s,t))
