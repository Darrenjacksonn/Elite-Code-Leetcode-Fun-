from typing import Optional

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def max_depth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        # define a recursion function that takes in a root and returns its depth.

        def recursion(node = root):

            # if the root is a leaf initiate its height to be 1
            if not node.left and not node.right:
                return 1
            
            left_depth , right_depth = 0 , 0

            # Stores the height of the current nodes left child 
            if node.left:
                left_depth = recursion(node.left) + 1
            
            # Stores the height of the current nodes right child
            if node.right:
                right_depth = recursion(node.right) + 1
            
            # Returns whatever height is larger, as we are only interested in the max height
            return max(left_depth, right_depth)
        
        return recursion()