# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0

        curr_val = 0
        if high >= root.val >= low:
            curr_val = root.val

        left = self.rangeSumBST(root.left, low, high)
        right = self.rangeSumBST(root.right, low, high)

        return left + right + curr_val
