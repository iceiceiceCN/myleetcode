# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        mindiff = float("inf")
        pre = float("inf")

        def search(root):
            nonlocal mindiff, pre # 只能在Python3里用
            if not root:
                return

            search(root.left)
            mindiff = min(mindiff, abs(root.val-pre))
            pre = root.val
            search(root.right)

        search(root)
        return mindiff

# 其实考察的是二叉搜索树的中序遍历，因为二叉搜索树的中序遍历结果是升序的，我们只需要在中序遍历的时候和前一个节点比较，保存最小的差值即可。
# nonlocal的用法就是使得子函数能调用外部函数的变量
# 中序遍历得到的一个有序数列，能够逐个对比差值