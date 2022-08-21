## Given an array arr[ ] of size N consisting of distinct integers, write a program that returns 1 if given array can represent preorder traversal of a possible BST, else returns 0.

def canRepresentBST(self, arr, N):
        stack = []
        root = float('-inf')
        for i in range(N):
            if arr[i] < root:
                return 0
            while stack and arr[i] > stack[-1]:
                root = stack.pop()
            stack.append(arr[i])
        return 1