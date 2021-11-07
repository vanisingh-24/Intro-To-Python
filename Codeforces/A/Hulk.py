'''
https://codeforces.com/problemset/problem/705/A
Solution: The idea is to alternate between "I hate" and "I love" phrases. Ever alternation is connected with a " that ".
And the final string ends with " it". 
'''

n = int(input())
 
even_phrase = 'I love'
odd_phrase = 'I hate'
connector = ' that '
finisher = ' it'
 
result = odd_phrase
 
for i in range(2,n+1):
  result += connector
 
  if i%2 == 0:
    result += even_phrase
  else:
    result += odd_phrase
 
result += finisher
 
print(result)