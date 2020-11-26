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

        queue = [(root, root.val)]

        while queue:
            node, val = queue.pop(0)
            if not node.left and not node.right and sum == val:
                return True

            if node.left:
                queue.append([node.left, val + node.left.val])
            if node.right:
                queue.append([node.right, val + node.right.val])

        return False

"""
BFS
BFS 使用 队列 保存遍历到每个节点时的路径和，如果该节点恰好是叶子节点，并且 路径和 正好等于 sum，说明找到了
"""