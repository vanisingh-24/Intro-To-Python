## Given two n-ary trees. 
## Check if they are mirror images of each other or not.
## You are also given e denoting the number of edges in both trees, and two arrays, A[] and B[].
## Each array has 2*e space separated values u,v denoting an edge from u to v for the both trees.

def checkMirrorTree(self, n, e, A, B):
        dict1 = {}
        dict2 = {}
        
        for i in range(0, 2*e, 2):
            if A[i] in dict1:
                dict1[A[i]].append(A[i+1])
            else:
                dict1[A[i]] = [A[i+1]]
            if B[i] in dict2:
                dict2[B[i]].append(B[i+1])
            else:
                dict2[B[i]] = [B[i+1]]
                
        for i in dict1:
            if dict1[i] != list(reversed(dict2[i])):
                return 0
        return 1