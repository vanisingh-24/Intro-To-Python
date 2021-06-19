# Given a number x, determine whether the given number is Armstrong number or not. 
# A positive integer of n digits is called an Armstrong number of order n (order is number of digits) if.

n = 153
sum = 0
order = len(str(n))
copy = n

while(n > 0 ):
  digit = n%10
  sum += digit**order
  n = n//10

if (sum == copy):
  print('Armstrong number')
else:
  print("Not Armstrong number")