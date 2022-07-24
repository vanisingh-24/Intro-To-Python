## Given a Binary Tree. Find the Zig-Zag Level Order Traversal of the Binary Tree.

# Using two stacks
class Solution:
    def zigZagTraversal(self, root):
        res = []
        current_level = [root]
        next_level = []
        flag=True
        while current_level:
            temp = current_level.pop()
            res.append(temp.data)
            if flag:
                if temp.left:
                    next_level.append(temp.left)
                if temp.right:
                    next_level.append(temp.right)
            else:
                if temp.right:
                    next_level.append(temp.right)
                if temp.left:
                    next_level.append(temp.left)
            if len(current_level) == 0:
                flag = not flag
                current_level,next_level = next_level,current_level
        return res
    
# Using queue

def zigZagTraversal(self, root):
        if root is None:
            return
        res = []
        queue = [root]
        flag=False
        while queue:
            n = len(queue)
            level = []
            for i in range(n):
                node = queue[0]
                queue.pop(0)
                level.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            flag = not flag
            if flag == False:
                level = level[::-1]
            for i in range(n):
                res.append(level[i])
        return res