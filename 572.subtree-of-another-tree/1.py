# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return True

        if not s or not t:
            return False

        return self.isSametree(s, t) or self.isSubtree(s.right, t) or self.isSubtree(s.left, t)

    def isSametree(self, s, t):
        if not s and not t:
            return True

        if not s or not t:
            return False

        return s.val == t.val and self.isSametree(s.left, t.left) and self.isSametree(s.right, t.right)
        # 如果两个树相等必须满足3个条件，即当前 node 的值相等，且各自左右子树也对应相等


"""
要判断一个树 t 是不是树 s 的子树，那么可以判断 t 是否和树 s 的任意子树相等。那么就转化成 100.Same Tree。
即，这个题的做法就是在 s 的每个子节点上，判断该子节点是否和 t 相等。

判断两个树是否相等的三个条件是*与*的关系，即：

1.当前两个树的根节点值相等；
2.并且，s 的左子树和 t 的左子树相等；
3.并且，s 的右子树和 t 的右子树相等。

而判断 t 是否为 s 的子树的三个条件是*或*的关系，即：

1.当前两棵树相等；
2.或者，t 是 s 的左子树；
3.或者，t 是 s 的右子树。
"""