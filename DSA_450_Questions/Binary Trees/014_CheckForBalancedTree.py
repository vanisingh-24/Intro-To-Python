## Given a binary tree, find if it is height balanced or not. 

class Solution:
    def isBalanced(self,root):
        
        def height(root):
            if not root:
                return [True, 0]
                
            left = height(root.left)
            right = height(root.right)
            balanced = (left[0] and right[0] and abs(left[1]-right[1]) <= 1)
            
            return [balanced, 1+max(left[1], right[1])]
            
        return height(root)[0]
    
# OR

def isBalanced(self,root):
        if root is None:
            return True
        left = self.isBalanced(root.left)
        right = self.isBalanced(root.right)
        if left == 0 or right == 0 or abs(left-right) > 1:
            return False
        return 1 + max(left, right)

