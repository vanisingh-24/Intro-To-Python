'''
https://codeforces.com/problemset/problem/469/A
Solution: Simply add all the indices Little X and Y in a set. The length of the set should be equal to n to make sure
their combined efforts can tackle all n levels of the game.
'''

def solve(n, p, q):
  levels = set()
  levels.update(p[1:])
  levels.update(q[1:])

  return "I become the guy." if len(levels) == n else "Oh, my keyboard!"

if __name__ == "__main__":
  n = int(input())
  p = input().split(' ')
  q = input().split(' ')
  print(solve(n, p, q))