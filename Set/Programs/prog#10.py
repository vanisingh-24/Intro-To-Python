# You are given a set A and N number of other sets.
# These N number of sets have to perform some specific mutation operations on set A.
# Your task is to execute those operations and print the sum of elements from set A.

n = int(input())
a = set(map(int, input().split()))
N  = int(input())
for i in range(N):
  cmd = input().split()
  s = set(map(int, input().split()))
  if (cmd[0]=='update'):
    a |= s
  elif(cmd[0]=='intersection_update'):
    a &= s
  elif(cmd[0]=='difference_update'):
    a -= s
  elif(cmd[0]=='symmetric_difference_update'):
    a ^= s
print(sum(a))
