# Kevin and Stuart want to play the 'The Minion Game'.

#Game Rules

# Both players are given the same string, S.
# Both players have to make substrings using the letters of the string S.
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.

# Scoring
# A player gets +1 point for each occurrence of the substring in the string S.
# Your task is to determine the winner of the game and their score.

def minion_game(s):
  s1 = 0
  s2 = 0
  vow = 'AEIOU'
  for i in range(len(s)):
    if s[i] not in vow:
      s1 = s1 + (len(s)-i)
    else:
      s2 = s2 + (len(s)-i)
  if s1 > s2:
    print("Stuart", s1)
  elif s2 > s1:
    print("Kevin", s2)
  else:
    print("Draw")

# Driver Code
s = input()
minion_game(s)


