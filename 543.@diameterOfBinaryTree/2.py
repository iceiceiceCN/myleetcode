# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def __init__(self): #如果有多个函数嵌套递归，可以使用__init__(self)来定义一个变量，持续记录
        self.max = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def depth(root):
            if not root:
                return 0
            l = depth(root.left)
            r = depth(root.right)

            self.max = max(r+l, self.max) # 拿当前节点的节点直径(左深度+右深度)去迭代比较最大直径

            return max(l, r) + 1 # 返回该节点的最大深度

        depth(root)
        return self.max