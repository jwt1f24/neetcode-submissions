# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.bal = True

        def dfs(curr):
            # base case, empty tree is balanced
            if curr is None:
                return 0

            leftHeight = dfs(curr.left)
            rightHeight = dfs(curr.right)

            # check if the height difference is greater or lesser than 1
            if abs(leftHeight - rightHeight) > 1:
                self.bal = False
            return 1 + max(leftHeight, rightHeight)

        dfs(root)
        return self.bal

        # time comp = O(n), time taken depends on the input size at worst case
        # space comp = O(n), memory usage depends on input size at worst case