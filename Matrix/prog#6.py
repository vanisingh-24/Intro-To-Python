## Matrix creation of n*n

# Using list comprehension
N = 4
print(N)

res = [list(range(1+N*i,1+N*(i+1))) for i in range(N)]

print(res)




