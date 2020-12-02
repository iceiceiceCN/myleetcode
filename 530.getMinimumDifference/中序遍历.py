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

# nonlocal的用法就是使得子函数能调用外部函数的变量