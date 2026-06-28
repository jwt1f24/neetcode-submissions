# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # check for matching nodes
        def sameTree(curr1, curr2):
            # base case, invalid if a node from root or subroot are empty
            if not curr1 and not curr2:
                return True
            elif not curr1 or not curr2:
                return False
            if curr1.val != curr2.val:
                return False
            return sameTree(curr1.left, curr2.left) and sameTree(curr1.right, curr2.right)

        # base case, invalid if root is empty
        if not root:
            return False
        return (sameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

        # time comp = O(m * n)
        # space comp = O(m + n)
        