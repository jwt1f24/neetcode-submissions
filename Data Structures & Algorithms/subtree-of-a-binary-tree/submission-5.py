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
            if curr1 is None and curr2 is None:
                return True
            elif curr1 is None or curr2 is None:
                return False
                
            if curr1.val != curr2.val:
                return False

            return sameTree(curr1.left, curr2.left) and sameTree(curr1.right, curr2.right)

        # base case, invalid if root is empty
        if root is None:
            return False

        # validate root & subroot
        return sameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        # time comp = O(m * n)
        # space comp = O(m + n)
        