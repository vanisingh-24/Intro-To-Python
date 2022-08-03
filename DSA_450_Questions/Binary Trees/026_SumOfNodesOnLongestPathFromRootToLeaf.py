## Given a binary tree of size N. Your task is to complete the function sumOfLongRootToLeafPath(), that find the sum of all nodes on the longest path from root to leaf node.
## If two or more paths compete for the longest path, then the path having maximum sum of nodes is being considered.

def sumOfLongRootToLeafPath(self,root):
        if (not root): 
            return 0
        maxSum = [-999999999999]
        maxLen = [0] 
        self.solve(root, 0, 0, maxLen, maxSum) 
        return maxSum[0]
        
def solve(self, root, Sum, Len,maxLen, maxSum):
        if (not root):
            if (maxLen[0] < Len): 
                maxLen[0] = Len
                maxSum[0] = Sum
                #print(maxLen[0])
                print(maxSum[0])
            elif (maxLen[0]== Len and maxSum[0] < Sum): 
                maxSum[0] = Sum
            return
 
        self.solve(root.left, Sum + root.data, Len + 1, maxLen, maxSum) 
        self.solve(root.right, Sum + root.data, Len + 1, maxLen, maxSum)
