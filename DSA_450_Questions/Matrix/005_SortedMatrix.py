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

N = 4
mat = [[10,20,30,40],[15,25,35,45],[27,29,37,48],[32,33,39,50]]
sortedMatrix(N, mat)