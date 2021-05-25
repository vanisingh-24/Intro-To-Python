# You are given two sets, A and B.
# Your job is to find whether set A is a subset of set B.
# If set A is subset of set B, print True.
# If set A is not a subset of set B, print False.

for i in range(int(input())):
  x = int(input())
  s1 = set(map(int, input().split()))
  y = int(input())
  s2 = set(map(int, input().split()))
  print(s1.issubset(s2)