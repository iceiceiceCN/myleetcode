# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = [(root.val, root, [root.val])]

        while queue:
            path, node, path_nodes = queue.pop(0)
            
            if node.left:
                queue.append((path+node.left.val, node.left,
                              path_nodes + [node.left.val]))
            if node.right:
                queue.append((path+node.right.val, node.right,
                              path_nodes + [node.right.val]))

            if not node.left and not node.right: # 如果是叶子节点
                if path == targetSum: # 如果满足条件
                    res.append(path_nodes)
        return res
