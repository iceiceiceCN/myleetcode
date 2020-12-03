"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0

        elif root.children == []: # root.children存储了一个包含所有子树的数组
            return 1

        else:
            height = [self.maxDepth(c) for c in root.children]

        return max(height) + 1

"""
递归：
复杂度分析

时间复杂度：每个节点遍历一次，所以时间复杂度是 O(N)，其中 N 为节点数。

空间复杂度：最坏情况下, 树完全非平衡，
例如 每个节点有且仅有一个孩子节点，递归调用会发生 N 次（等于树的深度），所以存储调用栈需要 O(N)。
但是在最好情况下（树完全平衡），树的高度为 log(N)。
所以在此情况下空间复杂度为 O(log(N))。


"""