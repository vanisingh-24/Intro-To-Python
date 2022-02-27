## Given a matrix mat[][] of size N x M, where every row and column is sorted in increasing order, and a number X is given.
## The task is to find whether element X is present in the matrix or not.

def matSearch(self,mat, N, M, X):
        i=0
        j=len(mat[0])-1
        
        while(i>=0 and i<len(mat) and j>=0 and j<len(mat[0])):
            if mat[i][j]==X:
                return 1
            
            else:
                if X<mat[i][j]:
                    j=j-1
                    
                else:
                    i=i+1
        return 0

# OR

def matSearch(mat, N, M, X):
	i = 0
    j = M - 1
    while ( i < N and j >= 0 ):
        if (mat[i][j] == X ):
            return 1
        if (mat[i][j] > X ):
            j -= 1
        else:
            i += 1
     
    return 0