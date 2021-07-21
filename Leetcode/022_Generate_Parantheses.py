# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Only add open paranthesis if open < n
        # Only add closed paranthesis if closed < open
        # calid if open == closed == n
        
        stack = []
        res = []
        
        def backtrack(open,closed):
            if open == closed == n:
                res.append("".join(stack))
                return
            
            if open < n:
                stack.append("(")
                backtrack(open+1, closed)
                stack.pop()
                
            if closed < open:
                stack.append(")")
                backtrack(open, closed+1)
                stack.pop()
                
        backtrack(0,0)
        return res
