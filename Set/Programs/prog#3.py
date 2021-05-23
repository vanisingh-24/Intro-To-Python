# Given 2 sets of integers, M and N, print their symmetric difference in ascending order.
# The term symmetric difference indicates those values that exist in either M or N but do not exist in both.

M = int(input())
set_M = set(map(int, input().split(' ')))

N = int(input())
set_N = set(map(int, input().split(' ')))

for element in sorted(set_M ^ set_N):
    print(element)
    