## Given a square matrix of size N x N. The task is to rotate it by 90 degrees in anti-clockwise direction without using any extra space. 

# rotate matrix anticlockwise by 90 degrees

def rotateby90(a, n): 
    for i in range(n//2):
        for j in range(i,n-i-1):
            temp = a[i][j]
            a[i][j] = a[j][n-i-1]
            a[j][n-i-1] = a[n-i-1][n-j-1]
            a[n-i-1][n-j-1] = a[n-j-1][i]
            a[n-j-1][i] = temp

    return a

# OR

def rotateby90(self,a, n): 
        for i in range(0,n):
            for j in range(i+1,n):
                a[i][j],a[j][i]=a[j][i],a[i][j]

        return a.reverse()

# OR

def rotate(matrix):
    for i in range(len(matrix)):
        matrix[i].reverse()

    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix[i][j]