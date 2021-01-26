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

        curr = [root]
        res = []
        while curr:
            temp = []
            n = len(curr)
            for i in range(n):
                node = curr.pop(0)
                temp.append(node.val)
                if node.left:
                    curr.append(node.left)
                if node.right:
                    curr.append(node.right)
            res.append(temp)

        return [res[i][::-1] if i % 2 == 1 else res[i]
                for i in range(len(res))]
