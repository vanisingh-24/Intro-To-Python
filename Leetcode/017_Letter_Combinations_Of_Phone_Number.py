# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
# Return the answer in any order.
# A mapping of digit to letters (just like on the telephone buttons) is given below.
# Note that 1 does not map to any letters.

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        # map of digits
        dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        if digits == "":
            return []
        
        output = [""]
        
        for d in digits:
            tmp = []
            for v in dict[d]:
                for o in output:
                    tmp.append(o+v)
            output = tmp
            
        return output

# OR

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        # map of digits
        digitsToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        # Recursive function 
        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            for c in digitsToChar[digits[i]]:
                backtrack(i+1, curStr+c)
            
        if digits:
            backtrack(0, "")
            
        return res
        