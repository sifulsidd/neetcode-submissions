# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findMin(root):
            curr = root
            while curr and curr.left:
                curr = curr.left
            return curr 
        
        if not root:
            return None 
        # go right if key is greater than value, and left if key is less than value  
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            # basically only 1 child on the right or left --> return the side that exists
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            # both children exist
            else:
                # find the minimum value from the right
                minNode = findMin(root.right)
                root.val = minNode.val
                # now we have to remvoe the min value from the right subtree
                root.right = self.deleteNode(root.right, minNode.val)
        return root