# Python program to split array and move first part to end.

def splitArr(arr, n, k):
	for i in range(0, k):
		d = arr[0]
		for j in range(0, n-1):
			arr[j] = arr[j + 1]
		
		arr[n-1] = d
		

# Driver Code

arr = [12, 10, 5, 6, 52, 36]
n = len(arr)
k = 2

splitArr(arr, n, k)

for i in range(0, n):
	print(arr[i], end = ' ')


# OR

def splitArray(a,n,k):
    b = a[:k]
    return (a[k::]+b[::])

# Driver Code

arr = [12,10,5,6,52,36]
n = len(arr)
k = 2
arr = splitArr(arr, n , k)
for i in range(0,n):
    print(arr[i], end=" ")