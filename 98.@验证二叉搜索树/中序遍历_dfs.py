# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        res = []
        def dfs(root):
            nonlocal res
            if not root:
                return []
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)

            return 
        dfs(root)
        res_ = sorted(set(res)) # 有相等的值就无法构成BST
        return res_ == res
