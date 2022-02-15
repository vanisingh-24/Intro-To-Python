## Given three arrays sorted in increasing order. Find the elements that are common in all three arrays.

# Simple solution

class Solution:
    def commonElements (self,A, B, C, n1, n2, n3):
       
        i, j, k = 0, 0, 0
        res = []
        
        while (i < n1 and j < n2 and k< n3):
            if (A[i] == B[j] and B[j] == C[k] and A[i] not in res):
                res.append(A[i])
                # print(A[i])
                i += 1
                j += 1
                k += 1
           
            elif A[i] < B[j]:
                i += 1
               
            elif B[j] < C[k]:
                j += 1
         
            else:
                k += 1
        return res