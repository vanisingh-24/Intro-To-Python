## Given an array A[] which represents a Complete Binary Tree i.e, if index i is the parent, index 2*i + 1 is the left child and index 2*i + 2 is the right child.
## The task is to find the minimum number of swaps required to convert it into a Binary Search Tree.

def minSwaps(self, n : int, A) -> int:
        ans = 0
        res = []
        temp = [0] * n
        map = {}
        
        self.inorder(A,n,0,res)
  
        for i in range(n):
            temp[i] = res[i]
            map[res[i]] = i
            
        temp.sort()
        
        i = 0
        
        while i < n:
            if res[i] == temp[i]:
                i += 1
            else:
                ans += 1
                
                index = map.get(temp[i])
                self.swap(i, index, temp)
                
        return ans
                
def swap(self,i,j,arr):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        


def inorder(self,arr, n, index,res):
        if index >= n:
            return
        
        self.inorder(arr,n, 2 * index + 1,res)
        res.append(arr[index])
        self.inorder(arr,n,2 * index + 2, res)