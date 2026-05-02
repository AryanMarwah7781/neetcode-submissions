# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p==None and q==None:
            return True
        if (p==None and q!=None) or (p!=None and q==None):
            return False
            
        p_queue=[p]
        q_queue=[q]
        while p_queue and q_queue:
            len_p=len(p_queue)
            len_q=len(q_queue)
            if len_p!=len_q:
                return False
            for i in range(0,len_p):
                p_root=p_queue.pop(0)
                q_root=q_queue.pop(0)
                if p_root and q_root:
                    if p_root.val != q_root.val:
                        return False
                else:
                    return False
                # Left child
            if (p_root.left is None) != (q_root.left is None):
                return False
            if p_root.left:
                p_queue.append(p_root.left)
                q_queue.append(q_root.left)

            # Right child
            if (p_root.right is None) != (q_root.right is None):
                return False
            if p_root.right:
                p_queue.append(p_root.right)
                q_queue.append(q_root.right)
                

        return True




            

            




        