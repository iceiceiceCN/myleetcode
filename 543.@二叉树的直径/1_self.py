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
        self.depth(root)
        return self.max

    def depth(self, root):
        if not root:
            return 0
        l = self.depth(root.left)
        r = self.depth(root.right)

        self.max = max(r+l, self.max) # 拿当前节点的节点直径(左深度+右深度)去迭代比较最大直径

        return max(l, r) + 1 # 返回该节点的最大深度

"""
二叉树的直径：二叉树中从一个结点到另一个节点最长的路径，叫做二叉树的直径
采用分治和递归的思想：
    - 根节点为root的二叉树的直径 = max(root->left的直径，root->right的直径，root->left的最大深度+root->right的最大深度+1)

二叉树上的任一“路径”上一定有一个结点是所有其他结点的祖先结点（因为“路径”是由一个个父子关系连接而成的），
那么换个表述方法，对于任一结点，以此结点为根的diameter就可以表示为[左子树高度 + 右子树高度]，而二叉树的diameter就是所有结点为根的diameter中最大的那个。


那么我得需要一个值来保存我这个每次比较更新的最大直径值，用self.max = 0来初始化这个值
在每次获得一个节点的左子树和右子树的值的时候，都需要比较一下self.max和左子树高度+右子树高度的大小，把更大的保存下来
然后如何求左子树和右子树的高度呢，那就是经典的递归求高度问题：max(depth(root.left), depth(root.right))+1
"""