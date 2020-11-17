# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        def dfs(left, right):
            # 递归的终止条件是两个节点都为空
            # 或者两个节点中有一个为空
            # 或者两个节点的值不相等
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            return dfs(left.left, right.right) and dfs(left.right, right.left)
        # 用递归函数，比较左节点，右节点
        return dfs(root.left, root.right)


"""
方法一：递归实现
根据题目的描述，镜像对称，就是左右两边相等，也就是左子树和右子树是相当的。
注意这句话，左子树和右子相等，也就是说要递归的比较左子树和右子树。
我们将根节点的左子树记做 left，右子树记做 right。比较 left 是否等于 right，不等的话直接返回就可以了。
如果相当，比较 left 的左节点和 right 的右节点，再比较 left 的右节点和 right 的左节点
比如看下面这两个子树(他们分别是根节点的左子树和右子树)，能观察到这么一个规律：
左子树 2 的左孩子 == 右子树 2 的右孩子
左子树 2 的右孩子 == 右子树 2 的左孩子

算法的时间复杂度是 O(n)，因为要遍历 n 个节点
空间复杂度是 O(n)，空间复杂度是递归的深度，也就是跟树高度有关，最坏情况下树变成一个链表结构，高度是n。
"""
