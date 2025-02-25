# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if root is None:
            return False
            # no path in this subtree ending

        remainingSum = targetSum - root.val
        # calculate the remaining value to check for
        # in left subtree / right subtree
        if root.left is None and root.right is None:
            return remainingSum == 0
            # return T/F weather
            # current node is the end of the path, or not.

        return (self.hasPathSum(root.left, remainingSum)) or (
            self.hasPathSum(root.right, remainingSum)
        )
        """
        Key: target = root + left/right + .. + leaf
             target - root = left/right + .. + leaf
             target - root-left/right = leaf
             SO 
             if leaf = target - root - left/right => RETURN TRUE
        
        Per node:
        if node is node => return FALSE, we've reached end of this 
        path witout a match, return False to the subtree

        if node is leaf => check if leaf.value == remaining_sum,
        return True/ false fro this subtree

        remaining_sum = target - leaf.value

        return recurse(left.node, remaining_sum) OR 
                recurse(right.node, remaining_sum)
        Here, we recurse on the right and left subtree 
        asking each node/subtree if it contains a child 
        node that contains the completion of the path to
        targetSum. Which is answered by checking if the child
        contains nothing but  
            target - current_node_value, sent as the new 'target'      
        """
