# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodNodesCounter = 0

        # helper returns nothing, just sends max to child nodes

        def helperDFS(root, maxValSoFar: int):
            nonlocal goodNodesCounter
            if root is None:
                # if we are at a leaf node, where left & right are empty
                # or root is empty:
                # do nothing, just return recursion
                return
            # send helper to left & right subtrees for post-order traversal
            helperDFS(root.right, max(root.val, maxValSoFar))
            helperDFS(root.left, max(root.val, maxValSoFar))

            # Now we deal with arbitrary node, X, by checking
            # if it's a good node, and updating ctr
            if root.val >= maxValSoFar:
                goodNodesCounter += 1
                maxValSoFar = root.val
            return

        # call helper & return global goodNodesCounter
        helperDFS(root, root.val)
        return goodNodesCounter
