## Given an array Arr of N positive integers. Your task is to find the elements whose value is equal to that of its index value ( Consider 1-based indexing ).

def valueEqualToIndex(arr, n):
    list = []
    for i in range(n):
        if i+1 == arr[i]:
            list.append(arr[i])
    return list