## Consider a sample space S consisting of all perfect squares starting from 1, 4, 9 and so on.
## You are given a number N, you have to output the number of integers less than N in the sample space S.

import math 

def countSquares(N):
    return math.floor(math.sqrt(N-1))

