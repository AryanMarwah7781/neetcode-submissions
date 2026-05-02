# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(root,subroot):
            if root is None and subroot is None:
                return True
            if root is None or subroot is None:
                return False
            if root.val!=subroot.val:
                return False
            return dfs(root.left,subroot.left) and dfs(root.right,subroot.right)
        def bfs(root,subroot):
            if root is None:
                return
            queue=deque([root])
            while queue:
                node=queue.popleft()
                if node.val == subRoot.val:
                    bool1=dfs(node,subRoot)
                    if bool1 is True:
                        return True
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            return False
        return bfs(root,subRoot)
                

        