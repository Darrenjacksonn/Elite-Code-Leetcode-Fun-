from typing import Optional

# Definition of TreeNode

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def leaf_similar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        if not root1 and not root2:
            return True
        
        # Define a recursive function that outputs a list -> The leaf value sequence of a tree with root -> node

        def recursive(node):
            
            # Checks if this node is a leaf, if it is, return its value in a list
            if not node.left and not node.right:
                return [node.val]

            left_leaf, right_leaf = [] , []

            # This will return this nodes left childs leaf sequence
            if node.left:
                left_leaf = recursive(node.left)
            
            # This will return this nodes right childs leaf sequence
            if node.right:
                right_leaf = recursive(node.right)
            
            # Return this nodes leaf sequence
            return left_leaf + right_leaf
                

        return recursive(root1) == recursive(root2)