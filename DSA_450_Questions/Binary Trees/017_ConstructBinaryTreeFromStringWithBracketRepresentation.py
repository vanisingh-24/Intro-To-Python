## Construct a binary tree from a string consisting of parenthesis and integers.
## The whole input represents a binary tree.
## It contains an integer followed by zero, one or two pairs of parenthesis.
## The integer represents the roots value and a pair of parenthesis contains a child binary tree with the same structure.
## Always start to construct the left child node of the parent first if it exists.

from typing import Optional

class Solution:
    def treeFromString(self, s : str) -> Optional['Node']:
        if not s:
            return None
            
        stack = []
        i = 0
        n = len(s)
        while i < n:
            if s[i].isdigit():
                num = 0
                while i < n and s[i].isdigit():
                    num = num*10 + int(s[i])
                    i += 1
                stack.append(Node(num))
                i -= 1
            elif s[i] == ')':
                curr = stack.pop()
                if stack:
                    parent = stack[-1]
                    if not parent.left:
                        parent.left = curr
                    else:
                        parent.right = curr
            i += 1
        return stack[0]
