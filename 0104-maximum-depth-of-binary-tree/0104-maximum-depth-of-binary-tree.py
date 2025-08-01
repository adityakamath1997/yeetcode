# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([(root, 1)])
        max_depth = 1
        while queue:

            node, depth = queue.popleft()
            if node.left:
                max_depth = max(depth+1, max_depth)
                queue.append((node.left, depth+1))
            if node.right:
                max_depth = max(depth+1, max_depth)
                queue.append((node.right, depth+1))
        return max_depth


        