# Given an integer, n and n space-separated integers as input, create a tuple, t, of those n integers.
# Then compute and print the result of hash(t).

n = int(input())
tup = tuple(map(int, input().split(' ')))
print (hash(tup))
