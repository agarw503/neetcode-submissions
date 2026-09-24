# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
    

        def dfs (node,maxb):
            if not node:
                return 0
            good = 1 if node.val >= maxb else 0
            maxb = max(node.val, maxb)
            return good + dfs(node.left, maxb) + dfs(node.right, maxb)
        return dfs(root, root.val)


            
        