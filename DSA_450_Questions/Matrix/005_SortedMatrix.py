## Given an NxN matrix Mat. Sort all elements of the matrix.

def sortedMatrix(self,N,Mat):
        ans=[]
        for i in range(N):
            for j in range(N):
                ans.append(Mat[i][j])
        ans.sort()
        x=0
        for i in range(N):
            for j in range(N):
                Mat[i][j]=ans[x]
                x+=1
       
        return Mat