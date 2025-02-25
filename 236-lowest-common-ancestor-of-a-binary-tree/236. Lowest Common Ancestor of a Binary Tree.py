# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":

        if root is None:
            return root

        leftFound = self.lowestCommonAncestor(root.left, p, q)
        rightFound = self.lowestCommonAncestor(root.right, p, q)

        if (leftFound and rightFound) or (root in [p,q]):
            return root
        else:
            return leftFound or rightFound
