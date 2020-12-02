# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        
        minD = 10**9
        if root.left:
            minD = min(self.minDepth(root.left),minD)
        if root.right:
            minD = min(self.minDepth(root.right),minD)
        
        return minD + 1

"""
方法一：深度优先搜索

首先可以想到使用深度优先搜索的方法，遍历整棵树，记录最小深度。
对于每一个非叶子节点，我们只需要分别计算其左右子树的最小叶子节点深度。
这样就将一个大问题转化为了小问题，可以递归地解决该问题。

这样想：存在一个二叉树[2,null,3]，它的最小深度是2，因为虽然左子树为空，但是右子树不为空，所以要按非空子树的最小深度来计算，

时间复杂度：O(N)，其中 N 是树的节点数。对每个节点访问一次。
空间复杂度：O(H)，其中 H 是树的高度。空间复杂度主要取决于递归时栈空间的开销，最坏情况下，树呈现链状，空间复杂度为 O(N)。
平均情况下树的高度与节点数的对数正相关，空间复杂度为O(logN)。

"""