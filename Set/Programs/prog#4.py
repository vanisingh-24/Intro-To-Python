# Rupal has a huge collection of country stamps.
# She decided to count the total number of distinct country stamps in her collection.
# She asked for your help.
# You pick the stamps one by one from a stack of N country stamps.
# Find the total number of distinct country stamps.

N = int(input())
stamp = set()

for i in range(N):
  stamp.add(input())
print(len(stamp))