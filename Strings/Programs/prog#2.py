# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

def split_and_join(s):
  return("-".join(s.split()))

s = input()
result = split_and_join(s)
print(result)