# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        res = 0
        def dfs(node):
            nonlocal count, res
            if not node:
                return 0
            # first go left 
            dfs(node.left)
            count += 1
            # check if count is equal to k
            if count == k:
                res = node.val
                return 
            # go right 
            dfs(node.right)
        dfs(root)
        return res