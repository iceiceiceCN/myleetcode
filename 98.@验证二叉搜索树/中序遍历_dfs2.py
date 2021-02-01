# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(root):
            if not root:
                return []

            return dfs(root.left) + [root.val] + dfs(root.right)

        res = dfs(root)
        res_ = sorted(set(res)) # 有相等的值就无法构成BST
        return res_ == res
