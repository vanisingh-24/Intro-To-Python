# Python program to run length encoding

from collections import OrderedDict

def runLengthEncoding(input):
  dict = OrderedDict.fromkeys(input, 0)

  for ch in input:
    dict[ch] += 1

  output = ''
  for key,value in dict.items():
    output = output + key + str(value)
  return output

# Driver Code
input="wwwwaaadexxxxxx"
print(runLengthEncoding(input))