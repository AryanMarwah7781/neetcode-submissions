# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.res=0
        def dfs(root):
            if root is None:
                return 0
            left=dfs(root.left)
            right=dfs(root.right)
            self.res=max(self.res,left+right)
            return 1 + max(left, right)
        res1=dfs(root)
        return self.res


        