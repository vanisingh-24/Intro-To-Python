## Given a sorted array arr containing n elements with possibly duplicate elements, the task is to find indexes of first and last occurrences of an element x in the given array.

def firstLast(arr, n, x):
    first_index = -1
    last_index = -1

    for i in range(0, n):
        if arr[i] == x:
            first_index = i
            break

    for i in range(n-1, -1, -1):
        if arr[i] == x:
            last_index = i
            break
    return first_index, last_index

arr = [1,3,5,5,5,5,67,123,125]
n = 9
x = 5
firstLast(arr, n, x)