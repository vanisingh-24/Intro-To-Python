## Given a binary tree of size  N, a node and a positive integer k
## Your task is to complete the function kthAncestor(), the function should return the kth ancestor of the given node in the binary tree.
## If there does not exist any such ancestor then return -1.

def solve(root,ans,node):
    if root==None:
        return False
    ans.append(root.data)
    if root.data==node:
        return True
        
    if solve(root.left,ans,node) or solve(root.right,ans,node):
        return True
    
    ans.pop()
    return False
            
def kthAncestor(root,k, node):
    ans=[]
    solve(root,ans,node)
    if len(ans)>k:
        return ans[len(ans)-k-1]
    else:
        return -1