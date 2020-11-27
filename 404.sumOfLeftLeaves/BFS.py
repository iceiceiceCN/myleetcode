# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        queue = [root]
        ans = 0
        while queue:
            node= queue.pop(0)
            if node.left:
                tmp = node.left
                if not tmp.left and not tmp.right:
                    ans += tmp.val
                else:
                    queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
        return ans
