## Given two integers M, N, and a 2D matrix Mat of dimensions MxN, clockwise rotate the elements in it.

class Solution:
    def rotateMatrix(self, M, N, Mat):
        top = 0
        bottom = len(Mat)-1

        left = 0
        right = len(Mat[0])-1

        while left < right and top < bottom:
            prev = Mat[top+1][left]

            for i in range(left, right+1):
                curr = Mat[top][i]
                Mat[top][i] = prev
                prev = curr
            top += 1

            for i in range(top, bottom+1):
                curr = Mat[i][right]
                Mat[i][right] = prev
                prev = curr
            right -= 1

            for i in range(right, left-1, -1):
                curr = Mat[bottom][i]
                Mat[bottom][i] = prev
                prev = curr
            bottom -= 1

            for i in range(bottom, top-1, -1):
                curr = Mat[i][left]
                Mat[i][left] = prev
                prev = curr
            left += 1

        return Mat