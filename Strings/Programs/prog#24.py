# SequenceMatcher in Python for Longest Common Substring

from difflib import SequenceMatcher

def longestSubstring(str1, str2):
  seqMatch = SequenceMatcher(None, str1, str2)

  match = seqMatch.find_longest_match(0, len(str1), 0, len(str2))

  if(match.size != 0):
    print(str1[match.a: match.a + match.size])
  else:
    print('No longest common sub-string found')

str1 = 'GeeksforGeeks'
str2 = 'GeeksQuiz'
longestSubstring(str1,str2)





