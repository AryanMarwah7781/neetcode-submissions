# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        height_r=1+self.maxDepth(root.right)
        height_l=1+self.maxDepth(root.left)
        return max(height_r,height_l)
        