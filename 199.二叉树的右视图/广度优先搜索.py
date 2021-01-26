# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        res = []
        queue = [root]

        while queue:
            n = len(queue)
            for _ in range(n):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                if _ == n-1:
                    res.append(node.val)

        return res

"""
思路:
我们可以对二叉树进行层次遍历，那么对于每层来说，最右边的结点一定是最后被遍历到的。
二叉树的层次遍历可以用广度优先搜索实现。

算法:
执行广度优先搜索，左结点排在右结点之前，这样，我们对每一层都从左到右访问。
因此，只保留每个深度最后访问的结点，我们就可以在遍历完整棵树后得到每个深度最右的结点。

时间复杂度 :O(n)。 每个节点最多进队列一次，出队列一次，因此广度优先搜索的复杂度为线性。
空间复杂度 :O(n)。 每个节点最多进队列一次，所以队列长度最大不不超过 n，所以这里的空间代价为 O(n)。

"""