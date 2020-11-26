# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # 递归函数的终止条件，节点为空时返回
        if not root:
            return None
        # 将当前节点的左右子树交换
        root.left,root.right = root.right,root.left
        # 递归交换当前节点的 左子树和右子树
        self.invertTree(root.left)
        self.invertTree(root.right)
		# 函数返回时就表示当前这个节点，以及它的左右子树
		# 都已经交换完了
        return root

"""
递归
我们在做二叉树题目时候，第一想到的应该是用 递归 来解决。
仔细看下题目的 输入 和 输出，输出的左右子树的位置跟输入正好是相反的，于是我们可以递归的交换左右子树来完成这道题。
时间复杂度：每个元素都必须访问一次，所以是 O(n)
空间复杂度：最坏的情况下，需要存放 O(h) 个函数调用(h是树的高度)，所以是 O(h)
"""