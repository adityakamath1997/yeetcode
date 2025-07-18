# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def mirror(n1, n2):
            if not n1 and not n2:
                return True
            
            if not n1 or not n2:
                return False

            return n1.val == n2.val and mirror(n1.left, n2.right) and mirror(n2.left, n1.right)
        
        return mirror(root.left, root.right)

        