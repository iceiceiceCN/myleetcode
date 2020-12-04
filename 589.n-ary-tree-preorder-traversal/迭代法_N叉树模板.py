"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        queue = [(root, root.val)]
        out = []

        while queue:
            node, val = queue.pop() # 由于是前序遍历，所以pop()，从最右边pop
            out.append(val)
            if node.children:
                for _node in node.children[::-1]: # 由于是前序遍历，把最左边的节点放在queue的最右边，方便pop
                    queue.append((_node, _node.val))

        return out
