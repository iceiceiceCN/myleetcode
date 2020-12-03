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

        queue = [(root, 1)]

        while queue:
            node, depth = queue.pop(0)

            if node.children:
                for _node in node.children:
                    queue.append((_node, depth + 1))

        return depth # BFS最后一个得到的depth就是最深的；时间O(N),空间O(N)
