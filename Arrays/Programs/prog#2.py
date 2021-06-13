# Python program to find the largest element in the array

def largest(arr, n):
   max = arr[0]

   for i in range(1,n):
     if arr[i]> max:
       max = arr[i]
   return max

# Driver Code
arr = [10,234,45,90]
n = len(arr)
res = largest(arr,n)
print(res)
