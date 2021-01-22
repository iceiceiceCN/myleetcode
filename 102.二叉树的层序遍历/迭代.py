# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue,res = [root], []
        while queue:
            tmp = []
            n = len(queue)
            for _ in range(n):
                node = queue.pop(0)
                if node.left:queue.append(node.left)
                if node.right:queue.append(node.right)
                tmp.append(node.val)
            res.append(tmp)
        return res