# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue1=[root]
        traversal_list=[]
        while queue1:
            temp1=[]
            for i in range(0,len(queue1)):
                node1=queue1.pop(0)
                temp1.append(node1.val)
                if node1.left:
                    queue1.append(node1.left)
                if node1.right:
                    queue1.append(node1.right)
            traversal_list.append(temp1)
        return traversal_list
            
                   



        