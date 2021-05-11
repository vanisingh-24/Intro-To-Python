# Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:
# 1. Mat size must be NXM. (N is an odd natural number, and M is 3 times N.)
# 2. The design should have 'WELCOME' written in the center.
# 3. The design pattern should only use |, . and - characters.

n,m = map(int,input().split())
s1 = '.|.'
s2 = 'WELCOME'

#PART 1
for i in range(n//2):
  print((s1*((i*2)+1)).center(m, '-'))

#PART 2
print(s2.center(m, '-'))

#PART 3
for i in range(n//2-1,-1,-1):
  print((s1*((i*2)+1)).center(m, '-'))


