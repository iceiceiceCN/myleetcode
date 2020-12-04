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

        stack = [root]
        out = []

        while stack:
            node = stack.pop()
            out.append(node.val)

            if node.children:
                # 由于是前序遍历，把最左边的节点放在stack的最右边，pop之后先拿到左节点，实现“中-左-右”
                for _node in node.children[::-1]:
                    stack.append(_node)

        return out