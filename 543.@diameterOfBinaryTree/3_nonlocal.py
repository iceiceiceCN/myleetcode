# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maxval = 0

        def depth(root):
            nonlocal maxval
            if not root:
                return 0
            # 通过左右dfs能得到每个节点的左右子树节点
            l = depth(root.left)
            r = depth(root.right)

            maxval = max(r+l, maxval)  # 拿当前节点的节点直径(左深度+右深度)去迭代比较最大直径

            return max(l, r) + 1  # 返回该节点的最大深度

        depth(root)
        return maxval
