# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diam = 0

        def dfs(curr):
            # base case, if tree is empty
            if curr is None:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)

            # get the max value between the current and largest diameter
            self.diam = max(self.diam, left + right)
            return 1 + max(left, right)
        dfs(root)
        return self.diam

        # time comp = O(n), time spent depends on input size
        # space comp = O(n), memory usage depends on input size