# The included code stub will read an integer, n , from STDIN.
# Without using any string methods, try to print the following:
# 123...n

n = int(input())
print(*range(1,n+1), sep="")

