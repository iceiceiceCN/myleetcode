# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        max_Depth = max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1
        return max_Depth

"""
时间复杂度：O(n)，其中 nn 为二叉树节点的个数。每个节点在递归中只被遍历一次。
空间复杂度：O(height)，其中 height 表示二叉树的高度。递归函数需要栈空间，而栈空间取决于递归的深度，因此空间复杂度等价于二叉树的高度。
"""