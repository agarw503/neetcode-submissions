# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def goodboy(node, maxb):
            if not node:
                return 0
            res =1 if node.val >= maxb else 0
            maxb = max(node.val, maxb)
            res += goodboy(node.left, maxb)
            res += goodboy(node.right, maxb)
            return res

        return goodboy(root, root.val)


            
        