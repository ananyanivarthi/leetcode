# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None :
            return []
        queue = deque()
        queue.append(root)
        result = []
        while queue:
            current_level = []
            level_size = len(queue)
            for i in range(level_size):
                root_node = queue.popleft()
                current_level.append(root_node.val)
                if root_node.left:
                    queue.append(root_node.left)
                if root_node.right:
                    queue.append(root_node.right)
            result.append(current_level)
        return result

