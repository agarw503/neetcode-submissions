# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def good (node, lkey, rkey):
            if not node:
                return True
            
            if  not(lkey < node.val < rkey):
                return False
            return good(node.left, lkey, node.val) and good(node.right, node.val,rkey)
        return good(root, float('-inf'), float('inf'))         