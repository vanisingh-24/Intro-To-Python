## Given an integer n. Return the nth row of the following look-and-say pattern.

# Recursion

class Solution:

    def lookandsay(self, n):
        if n == 1:
            return "1"
        s = self.lookandsay(n-1)
        counter = 0
        res = ""
        for i in range(0, len(s)):
            counter += 1
            if (i == len(s)-1) or s[i] != s[i+1]:
                res = res + str(counter) + s[i]
                counter = 0
        return res
