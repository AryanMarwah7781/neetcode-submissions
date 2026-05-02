# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isDFS(root,low,high):
            if not root:
                return True 
            else:
                if not(low<root.val<high):
                    return False
            dfs_left=isDFS(root.left,low,root.val)
            dfs_right=isDFS(root.right,root.val,high)
            return dfs_left and dfs_right
        return isDFS(root,float("-inf"), float("inf"))
            


        

        