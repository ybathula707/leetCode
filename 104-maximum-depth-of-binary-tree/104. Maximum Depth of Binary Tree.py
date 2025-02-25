# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return -1
        # null node
        elif root.left is None and root.right is None:
            return 1
        # leaf node
        """
            elif saves on SPACE complexity,
            one less evaluation per recursive call
        """
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        return max(leftDepth, rightDepth) + 1



        """ 
        root    3
               / \
               9  20
                 /  \
                15  7
                / \
               18  ghost
        How to solve this problem in the context of subtree instacnces.
        That is, once we get to the smaller problem of a single node,
        how can we answer the prompt?
        per node,x, to find max depht we need:
        - depth of left tree, depth of right tree
            - between the max of the two, we can add +1 to account
            for the depth of the current node & recurse to the parent
            - return max(leftDepth, rightDepth) +1
        - Base 
            1. node is None:
                return 0 
                ( there's no depth to increment)
                reached when we traverse an empty subtree in a 
                recursive call
            2. node is LEAF (node.left & node.right == None):
                return 1 (height of current node)
        - Left/Right:
            Leftdepth = maxDepth(node.Left)
            RightDepth = maxDept(node.Right)
            We simply just send the recursion to each subtree.
            Once returned, they will hold their representation
            of the return stateemnt, which basically means
            they will contain the maximum depth from their respective
            subtree
                => returned max(right,left) +1

        """
