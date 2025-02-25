# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        max_uni_path = 0

        def dfs(root):
            nonlocal max_uni_path
            if root is None:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            leftArrow = 0
            rightArrw = 0

            if root.left and root.left.val == root.val:
                leftArrow = left + 1
            if root.right and root.right.val == root.val:
                rightArrw = right + 1

            max_uni_path = max(leftArrow + rightArrw, max_uni_path)
            return max(leftArrow, rightArrw)
        dfs(root)
        return max_uni_path

    """
    Subproblem:
        - longest univalue path Left subtree
        - longest univalue path right subtree
        - if  current node is univalue node
    Globally: longest uni path

    in helper(root, root.value):
        find longest path left/right
        add them and update current IF curr node = root.value
        reutrn max of left right + 1 if current is univalue
        IF NOT:
            return 0 to parent
    """
