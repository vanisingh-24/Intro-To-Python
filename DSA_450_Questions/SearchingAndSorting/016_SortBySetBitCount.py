## Given an array of integers, sort the array (in descending order) according to count of set bits in binary representation of array elements. 

class Solution:
    def sortBySetBitCount(self, arr, n):
        return arr.sort(reverse = True, key = lambda x: bin(x).count('1'))

        