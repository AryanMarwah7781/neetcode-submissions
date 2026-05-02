# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue=[root]
        list1=[]
        while queue:
            size_queue=len(queue)
            for i in range(0,len(queue)):
                node1=queue.pop(0)
                print("Position " + str(i)+ ":"+ str(node1.val))
                if i==size_queue-1:
                    list1.append(node1.val)
                if node1.left:
                    queue.append(node1.left)
                if node1.right:
                    queue.append(node1.right)
        return list1
                

        
        