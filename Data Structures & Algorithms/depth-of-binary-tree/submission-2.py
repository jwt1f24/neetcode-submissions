# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # base case, if tree is empty
        if root is None:
            return 0
        
        # depth-first search, find each sides' depth and compare to find greater depth
        left = 1 + self.maxDepth(root.left)
        right = 1 + self.maxDepth(root.right)
        return max(left, right)

        # time comp = O(n), time spent is based on input size at worst case
        # space comp = O(n), memory usage is based on each recursion call at worst case