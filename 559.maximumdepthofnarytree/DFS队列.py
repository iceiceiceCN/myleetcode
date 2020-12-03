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
        max_depth = -1
        queue = [(root, 1)]
        while queue:
            node, depth = queue.pop(0)
            max_depth = max(depth, max_depth)

            if node.children:
                for _node in node.children:
                    queue.append((_node, depth+1))

        return max_depth
