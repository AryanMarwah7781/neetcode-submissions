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
        # recurse on left and right via self
        left_depth  = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        # 1 for the current node, plus the deeper of the two
        return 1 + max(left_depth, right_depth)

        

        