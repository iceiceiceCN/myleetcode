# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        def getpath(root, target):
            path = list()
            node = root
            path.append(node)
            while node != target:
                if target.val > node.val:
                    node = node.right
                else:
                    node = node.left
                path.append(node)
            return path
        path_p = getpath(root,p)
        path_q = getpath(root,q)
        
        ans = -1
        for k,v in zip(path_p,path_q):
            if k == v:
                ans = k
            else:
                continue
        
        return ans
"""
方法一：两次遍历
先找到p和q，并记录路径，然后比较路径上相同的节点。
思路与算法

注意到题目中给出的是一棵「二叉搜索树」，因此我们可以快速地找出树中的某个节点以及从根节点到该节点的路径，
例如我们需要找到节点 p：我们从根节点开始遍历；如果当前节点就是 p，那么成功地找到了节点；

如果当前节点的值大于 p 的值，说明 p 应该在当前节点的左子树，因此将当前节点移动到它的左子节点；
如果当前节点的值小于 p 的值，说明 p 应该在当前节点的右子树，因此将当前节点移动到它的右子节点。

对于节点 q 同理。在寻找节点的过程中，我们可以顺便记录经过的节点，这样就得到了从根节点到被寻找节点的路径。
当我们分别得到了从根节点到 p 和 q 的路径之后，我们就可以很方便地找到它们的最近公共祖先了。
显然，p 和 q 的最近公共祖先就是从根节点到它们路径上的「分岔点」，也就是最后一个相同的节点。
因此，如果我们设从根节点到 p 的路径为数组 path_p[]，从根节点到 q 的路径为数组 path_q[]，
那么只要找出最大的编号 i，其满足path_p[i]=path_q[i],那么对应的节点就是「分岔点」，即 p 和 q 的最近公共祖先就是 path_p[i]（或path_q[i]）。


时间复杂度：O(n)，其中 n 是给定的二叉搜索树中的节点个数。上述代码需要的时间与节点 p 和 q 在树中的深度线性相关，
而在最坏的情况下，树呈现链式结构，p 和 q 一个是树的唯一叶子结点，一个是该叶子结点的父节点，此时时间复杂度为 Θ(n)。
空间复杂度：O(n)，我们需要存储根节点到 p 和 q 的路径。和上面的分析方法相同，在最坏的情况下，路径的长度为 Θ(n)，因此需要 Θ(n) 的空间。

"""