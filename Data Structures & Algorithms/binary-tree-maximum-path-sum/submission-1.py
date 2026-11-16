# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        # can go left
        # can go right 
        # don't split
        def dfs(root):
            if not root:
                return 0 
            
            left = dfs(root.left)
            right = dfs(root.right)
            leftMax = max(left, 0) # ignores negative path
            rightMax = max(right, 0) # ignores negative path

            # updates global result with best pass through the nodes
            res[0] = max(res[0], root.val + leftMax + rightMax)
            return root.val + max(leftMax, rightMax)
        
        dfs(root)
        return res[0]
