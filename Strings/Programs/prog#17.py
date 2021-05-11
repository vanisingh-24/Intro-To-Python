# You are given a string S and width w.
# Your task is to wrap the string into a paragraph of width w.

import textwrap

def textWrap(string, max_width):
  return textwrap.fill(string, max_width)

string = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
max_width = 4
print(textWrap(string, max_width))



