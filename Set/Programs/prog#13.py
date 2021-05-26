# You are given a set A and n other sets.
# Your job is to find whether set A is a strict superset of each of the N sets.
# Print True, if A is a strict superset of each of the N sets.
# Otherwise, print False.
# A strict superset has at least one element that does not exist in its subset.

A = set(input().split())
n = int(input())
check = True
for i in range(n):
  s = set(input().split())
  if (s&A != s) or (s == A):
    check = False
    break
print(check)