# You have a non-empty set s, and you have to execute N commands given in N lines.
# The commands will be pop, remove and discard.
# Print the sum of the elements of set s on a single line.

n = int(input())
s = set(map(int, input().split()))
commands = int(input())

for i in range(commands):
  cmd = list(input().split(' '))
  if cmd[0]=='pop':
    s.pop()
  elif cmd[0]=='remove':
    s.remove(int(cmd[1]))
  elif cmd[0]=='discard':
    s.discard(int(cmd[1]))

print(sum(s))
