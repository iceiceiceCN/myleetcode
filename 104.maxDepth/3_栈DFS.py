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
        
        stack = [(1,root)]
        depth = 0
        while stack:
            cur_depth,node = stack.pop()
            depth = max(cur_depth,depth)
            if node.left:
                stack.append((cur_depth+1,node.left))
            if node.right:
                stack.append((cur_depth+1,node.right))
        
        return depth

"""
DFS与BFS有两点不同：

最后得到的深度不一定是最大深度，所以要用max判断
DFS（先序遍历）节点右孩子先入栈，左孩子再入栈
"""