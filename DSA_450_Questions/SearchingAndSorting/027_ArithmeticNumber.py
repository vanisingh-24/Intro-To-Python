## Given three integers  'A' denoting the first term of an arithmetic sequence , 'C' denoting the common difference of an arithmetic sequence and an integer 'B'. you need to tell whether 'B' exists in the arithmetic sequence or not.

# Simple Solution

class Solution:
    def inSequence(self, A, B, C):
        if A == B:
            return 1
        if C == 0:
            if A == B:
                return 1
            else:
                return 0
        if ((B-A)%C == 0 and (B-A)/C > 0):
            return 1
        else:
            return 0

# OR (neat code)

class Solution:
    def inSequence(self, A, B, C):
        if C == 0:
            if A == B:
                return 1
            else:
                return 0
        if (B-A)/C < 0:
            return 0
        if (B-A)%C == 0:
            return 1
        return 0
