"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        stack = [root]
        out = []

        while stack:
            node = stack.pop()
            out.append(node.val)

            if node.children:
                # 由于是后序遍历，把左右节点按顺序加入stack中，pop之后先拿到右节点，实现“中-右-左”
                for _node in node.children:
                    stack.append(_node)
            
        
        return out[::-1] # 将“中-右-左”倒序输出得到“左-右-中”，即后序遍历

"""
在后序遍历中，我们会先遍历一个节点的所有子节点，再遍历这个节点本身。例如当前的节点为 u，它的子节点为 v1, v2, v3 时，
那么后序遍历的结果为 [children of v1], v1, [children of v2], v2, [children of v3], v3, u，
其中 [children of vk] 表示以 vk 为根节点的子树的后序遍历结果（不包括 vk 本身）。

我们将这个结果反转，可以得到 u, v3, [children of v3]', v2, [children of v2]', v1, [children of v1]'，
其中 [a]' 表示 [a] 的反转。此时我们发现，结果和前序遍历非常类似，只不过前序遍历中对子节点的遍历顺序是 v1, v2, v3，而这里是 v3, v2, v1。

因此我们可以使用和 N叉树的前序遍历 相同的方法，使用一个栈来得到后序遍历。我们首先把根节点入栈。当每次我们从栈顶取出一个节点 u 时，就把 u 的所有子节点顺序推入栈中。
例如 u 的子节点从左到右为 v1, v2, v3，那么推入栈的顺序应当为 v1, v2, v3，这样就保证了下一个遍历到的节点（即 u 的第一个子节点 v3）出现在栈顶的位置。
在遍历结束之后，我们把遍历结果反转，就可以得到后序遍历。

"""