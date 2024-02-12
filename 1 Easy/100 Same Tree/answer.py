from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def is_same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # If there is no nodes in both trees at this point, they have indentical structure at this point
        if not p and not q:
            return True
        
        # If one node exists without the other, or if their values are not the same, they are not \n
        # structurally identical
        if not p or not q or p.val != q.val:
            return False
        
        # check the above for every descendent 
        return self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)
    



    
root1 = TreeNode(4)
root2 = TreeNode(4)

root1.left = TreeNode(2)
root2.left = TreeNode(2)

root1.left.left = TreeNode(-5)
root2.left.left = TreeNode(-5)

root1.right = TreeNode(0)
root2.right = TreeNode(0)

# Both trees have the following structure [4, 2, 0, -5, Null, Null, Null, Null]

sol = Solution()
print(sol.is_same_tree(root1,root2)) # True

root1.left.right = TreeNode(7)
print(sol.is_same_tree(root1,root2)) # False
