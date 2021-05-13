# python program to Check if there are K consecutive 1’s in a binary number

def check(s,k):
  new="1"*k

  if new in s:
    print("yes")
  else:
    print("No")

# Driver Code
s = "10101001111"
k = 4
check(s,k)