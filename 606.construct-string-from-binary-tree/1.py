# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def tree2str(self, t: TreeNode) -> str:
        res = ''

        def helper(root):
            if not root:
                return ''

            if root.left and not root.right:
                return str(root.val) + '(' + helper(root.left) + ')'

            if not root.left and root.right:
                return str(root.val) + '()' + '(' + helper(root.right) + ')'

            if not root.left and not root.right:
                return str(root.val)

            if root.left and root.right:
                return str(root.val) + '(' + helper(root.left) + ')' + '(' + helper(root.right) + ')'

        res = helper(t)
        return res
