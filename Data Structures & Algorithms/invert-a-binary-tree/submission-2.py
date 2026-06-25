# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # base case, if tree is empty
        if root is None:
            return root
        
        # swap child nodes
        temp1 = root.right
        root.right = root.left
        root.left = temp1

        # recurse
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

        # time comp = O(n)
        # space comp = O(n)