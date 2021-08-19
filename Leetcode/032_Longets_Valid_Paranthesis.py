# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        mx = 0
        
        for i, p in enumerate(s):
            if p == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    mx = max(mx, i-stack[-1])
                
        return mx

# OR

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l, r = 0, 0
        mx = 0
        
        for p in s:
            if p == '(':
                l += 1
            else:
                r += 1
            if l == r:
                mx = max(mx,r*2)
            elif r > l:
                l,r = 0,0
        l, r = 0, 0
        for p in reversed(s):
            if p == ')':
                r += 1
            else:
                l += 1
            if l == r:
                mx = max(mx,r*2)
            elif l > r:
                l,r = 0,0
        return mx