## Given a Integer array A[] of n elements
## Your task is to complete the function PalinArray.
## Which will return 1 if all the elements of the Array are palindrome otherwise it will return 0.

def PalinArray(arr ,n):
    for i in arr:
        if str(i) != str(i)[::-1]:
            return 0
    return 1

