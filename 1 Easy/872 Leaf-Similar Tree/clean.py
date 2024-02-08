from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leaf_similar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        if not root1 and not root2:
            return True

        def recursive(node):
            
            if not node.left and not node.right:
                return [node.val]

            left_leaf, right_leaf = [] , []

            if node.left:
                left_leaf = recursive(node.left)
            
            if node.right:
                right_leaf = recursive(node.right)
            
            return left_leaf + right_leaf
                
        return recursive(root1) == recursive(root2)