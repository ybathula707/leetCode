# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        def dfs(root):
            nonlocal max_depth
            if root is None:
                return 0
            if root.right is None and root.left is None:
                return 1

            left = dfs(root.left)
            right = dfs(root.right)

            curr_longest = left + right 

            max_depth = max(max_depth, curr_longest)

            return  max(left, right ) + 1
        dfs(root)
        return max_depth    
        