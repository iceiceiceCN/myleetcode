# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = [root]
        flag = 0
        while queue:
            tmp = []
            size = len(queue)
            for _ in range(size):
                node = queue.pop(0)
                tmp.append(node.val)
                if node.left:queue.append(node.left)
                if node.right:queue.append(node.right)
            if flag%2 == 0:
                res.append(tmp)
            elif flag%2 != 0:
                res.append(tmp[::-1])
            flag += 1
        return res
            


