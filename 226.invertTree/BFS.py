# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        
        queue = [root]
        while queue:
            node = queue.pop(0)
            if not node.left and not node.right:
                continue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            node.left,node.right = node.right,node.left
        
        return root
"""
迭代
递归实现也就是深度优先遍历的方式，那么对应的就是广度优先遍历。
广度优先遍历需要额外的数据结构--队列，来存放临时遍历到的元素。
深度优先遍历的特点是一竿子插到底，不行了再退回来继续；而广度优先遍历的特点是层层扫荡。
所以，我们需要先将根节点放入到队列中，然后不断的迭代队列中的元素。
对当前元素调换其左右子树的位置，然后：

判断其左子树是否为空，不为空就放入队列中
判断其右子树是否为空，不为空就放入队列中

时间复杂度：同样每个节点都需要入队列/出队列一次，所以是 O(n)
空间复杂度：最坏的情况下会包含所有的叶子节点，完全二叉树叶子节点是 n/2个，所以时间复杂度是 0(n)
"""