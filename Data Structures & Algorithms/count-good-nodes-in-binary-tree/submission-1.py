# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0

        res = 0
        queue = deque([(root, root.val)])  # (node, max_so_far)

        while queue:
            node, max_v = queue.popleft()

            # current node is good if its value >= max so far
            if node.val >= max_v:
                res += 1

            new_max = max(max_v, node.val)

            if node.left:
                queue.append((node.left, new_max))
            if node.right:
                queue.append((node.right, new_max))

        return res
            
            
            


        
            

        