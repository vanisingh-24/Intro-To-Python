# You are given a string s and an array of strings words of the same length.
# Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.
# You can return the answer in any order.

class Solution:
    def findSubstring(self, s, words):

        if len(words) == 0: return []
        wordsDict = {}
        for word in words:  # Count the number of occurrences of each word
            if word not in wordsDict:
                wordsDict[word] = 1
            else:
                wordsDict[word] += 1

        n, m, k = len(s), len(words[0]), len(words)  # n, m, k respectively, the length of the string, the length of the word, the number of words
        res = []

        for i in range(n - m * k + 1):  # Select an interval or window
            j = 0
            cur_dict = {}

            while j < k:
                word = s[i + m * j:i + m * j + m]  # 
                if word not in wordsDict:  # appears a word that does not exist, directly end this interval
                    break
                if word not in cur_dict:
                    cur_dict[word] = 1
                else:
                    cur_dict[word] += 1
                if cur_dict[word] > wordsDict[word]:  # A word is greater than necessary, then directly end this interval
                    break
                j += 1  # 

            print(j)
            if j == k: res.append(i)  # Record starting position

        return res

