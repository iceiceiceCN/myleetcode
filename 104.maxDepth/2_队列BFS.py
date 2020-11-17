# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        queue = [(1,root)]
        while queue:
            depth,node = queue.pop(0)
            if node.left:
                queue.append((depth+1,node.left))
            if node.right:
                queue.append((depth+1,node.right))
        
        return depth
"""
非递归BFS，层次遍历最后得到的深度就是最大的深度
"""