## Backward Iteration

#1 Using reversed()

N = 6

for num in reversed(range(N + 1)):
    print(num, end = " ")

# Using range(N, -1, -1)

N = 6

for num in range(N, -1, -1):
    print(num, end=" ")