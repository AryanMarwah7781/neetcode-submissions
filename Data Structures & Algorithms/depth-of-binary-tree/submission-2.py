# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def calcDepth(self,root):
        if not root:
            return 0
        left=1+self.calcDepth(root.left)
        right=1+self.calcDepth(root.right)
        return max(left,right)

        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        val=self.calcDepth(root)
        return val


        