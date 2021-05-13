# Concatenated string with uncommon characters in Python

def concat(str1, str2):

  s1 = set(str1)
  s2 = set(str2)

  common = list(s1 & s2)

  result = [ch for ch in str1 if ch not in common] + [ch for ch in str2 if ch not in common]

  print("".join(result))

# Driver Code
str1 = 'aacdb'
str2 = 'gafd'
concat(str1, str2)