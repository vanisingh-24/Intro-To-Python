## Given a Binary Search Tree and a node value X, find if the node with value X is present in the BST or not.

def search(self, node, x):
        if node is None or node.data == x:
            return node
        
        if node.data < x:
            return self.search(node.right, x)
        return self.search(node.left, x)