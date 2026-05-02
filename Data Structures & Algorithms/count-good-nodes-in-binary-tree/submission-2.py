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
        res = 1
        queue = deque([(root, root.val)])
        while queue:
            node, max_v = queue.popleft()
            if node.left:
                print(" Node Left Val: " + str(node.left.val))
                print("max_v: " + str(max_v))
                if node.left.val < max_v:
                    queue.append((node.left, max_v))
                else:
                    queue.append((node.left, node.left.val))
                    res += 1
            if node.right:
                if node.right.val < max_v:
                    queue.append((node.right, max_v))
                else:
                    queue.append((node.right, node.right.val))
                    res += 1
        return res
            
            
            


        
            

        