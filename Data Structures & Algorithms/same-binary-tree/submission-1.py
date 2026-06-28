# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(curr1, curr2):
            # base case, not same if a tree is empty
            if curr1 is None and curr2 is None:
                return True
            elif curr1 is None or curr2 is None:
                return False

            # base case, not same if both nodes have different values
            if curr1.val != curr2.val:
                return False

            # return left & right child nodes via recursion
            return dfs(curr1.left, curr2.left) and dfs(curr1.right, curr2.right)
        return dfs(p, q)
            
        # time comp = O(n), time spent depends on input size at worst case
        # space comp = O(n), memory used depends on input size at worst case