# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.count=0
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node1,currentMax):
            if not node1:
                return 
            if node1.val>=currentMax:
                self.count+=1
                currentMax=node1.val
            dfs(node1.left,currentMax)
            dfs(node1.right,currentMax)
        dfs(root,root.val)
        return self.count

        