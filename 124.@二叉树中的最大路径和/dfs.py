# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        maxSum = float('-inf')

        def dfs(root):
            nonlocal maxSum
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            maxSum = max(maxSum, root.val + left + right)
            # 返回当前节点作为根节点的最大收益路线，两边都走

            return max(0, max(left, right) + root.val)
            # 返回当前节点的单边最大收益路线，不能两边都走
            # 只需要告诉上一层，当前节点往左走还是往右走收益大，因为需要递归给上一层继续计算
            # 因为节点值有可能是负数，如果是负数的话则直接舍弃，返回0

        dfs(root)
        return maxSum
