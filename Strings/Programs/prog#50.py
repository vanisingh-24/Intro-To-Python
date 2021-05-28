# String slicing in Python to rotate a string

def rotate(input, d):
  Lfirst = input[0:d]
  Lsecond = input[d:]
  Rfirst = input[0: len(input)-d]
  Rsecond = input[len(input)-d:]

  print("Left Rotation:", (Lsecond+ Lfirst))
  print("Right Rotation:", (Rsecond+ Rfirst))

# Driver Code
input = "GeeksForFeeks"
d = 2
rotate(input,d)
