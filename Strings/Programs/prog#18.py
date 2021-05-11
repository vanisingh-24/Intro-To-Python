# Given an integer, n , print the following values for each integer i from 1 to n:
# 1. Decimal
# 2. Octal
# 3. Hexadecimal (capitalized)
# 4. Binary

def string_formatting(number):
  w = len(str(bin(number))[2:])
  for i in range(1, number+1):
    print(str(i).rjust(w, ' '),oct(i)[2:].rjust(w, ' '),hex(i)[2:].upper().rjust(w, ' '),bin(i)[2:].rjust(w, ' '))

n = int(input())
string_formatting(n)
