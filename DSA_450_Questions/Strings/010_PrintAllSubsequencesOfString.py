## Given a string, we have to find out all subsequences of it.

# Bit Manipulation

import math
class Solution:
	def AllPossibleStrings(self, s):
	    res = []
	    set_size = len(s)
	    n = (int)(math.pow(2, set_size))
	    for i in range(1, n):
	        x = i
	        j = 0
	        c = ""
	        while x:
	            if x & 1:
	                c = c + s[j]
	            j += 1
	            x = x>>1
	        res.append(c)
	    res.sort()
	    return res

