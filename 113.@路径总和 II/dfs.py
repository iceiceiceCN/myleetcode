# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int):
        res = []

        def dfs(root, targetSum, path):
            if not root:  # 空节点，不做处理
                return

            if not root.left and not root.right:  # 叶子节点
                if targetSum == root.val:  # 剩余的「路径和」恰好等于叶子节点值
                    res.append(path + [root.val])  # 把该路径放入结果中

            dfs(root.left, targetSum - root.val, path + [root.val])  # 左子树
            dfs(root.right, targetSum - root.val, path + [root.val])  # 右子树

        dfs(root, targetSum, [])
        return res
