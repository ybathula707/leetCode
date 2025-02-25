# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        globalTilt =0
        def helperTilt(root):
            if root is None: 
                return 0
            if root.left is None and root.right is None:
                return root.val

            nonlocal globalTilt

            leftSum = helperTilt(root.left)
            rightSum = helperTilt(root.right)
            globalTilt += abs(leftSum - rightSum)

            return leftSum + rightSum + root.val

        helperTilt(root) 
        return globalTilt
