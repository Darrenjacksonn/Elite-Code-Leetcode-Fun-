from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def max_depth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        def recursion(node = root):

            if not node.left and not node.right:
                return 1
            
            left_depth , right_depth = 0 , 0

            if node.left:
                left_depth = recursion(node.left) + 1
            if node.right:
                right_depth = recursion(node.right) + 1
            
            return max(left_depth, right_depth)
        
        return recursion()