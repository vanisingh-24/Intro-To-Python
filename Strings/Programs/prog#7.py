# You are given a partial code that is used for generating the HackerRank Logo of variable thickness.
# Your task is to replace the blank (______) with rjust, ljust or center.

thickness = 5
c = 'H'

# TOP CONE
for i in range(thickness):
  print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

# TOP PILLARS
for i in range(thickness+1):
  print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# MIDDLE BELT
for i in range((thickness+1)//2):
  print((c*thickness*5).center(thickness*6))

# BOTTOM PILLARS
for i in range(thickness+1):
  print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# BOOTOM CONE
for i in range(thickness):
  print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

