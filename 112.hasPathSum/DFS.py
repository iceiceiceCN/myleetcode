# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right:
            return sum == root.val

        return (self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val))

"""
DFS
首先是 DFS 解法，该解法的想法是一直向下找到叶子节点，如果到叶子节点时sum == 0，说明找到了一条符合要求的路径
当题目中提到了叶子节点时，正确的做法一定要同时判断节点的左右子树同时为空才是叶子节点。
"""