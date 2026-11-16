# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        total = float("-inf")
        res = [root.val]
        # can go left
        # can go right 
        # don't split
        def dfs(root):
            if not root:
                return 0 
            
            left = dfs(root.left)
            right = dfs(root.right)
            leftMax = max(left, 0) # indicates whether our value is greater than 0 or not in case of negative
            rightMax = max(right, 0)

            # compute max sub WITH split
            res[0] = max(res[0], root.val + leftMax + rightMax)
            return root.val + max(leftMax, rightMax)
        
        dfs(root)
        return res[0]
