# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.recur(root) != -1

    def recur(self,root):
        if not root:
            return 0
        
        left = self.recur(root.left)
        if left == -1:return -1
        right = self.recur(root.right)
        if right == -1:return -1

        return max(left,right) + 1 if abs(left-right) <2 else -1
"""
从底至顶：
思路是对二叉树做先序遍历，从底至顶返回子树最大高度，若判定某子树不是平衡树则 “剪枝” ，直接向上返回。

recur(root):

递归返回值：
当节点root 左 / 右子树的高度差 < 2 ：则返回以节点root为根节点的子树的最大高度，即节点 root 的左右子树中最大高度加 1 （ max(left, right) + 1 ）；
当节点root 左 / 右子树的高度差 >= 2 ：则返回 −1 ，代表此子树不是平衡树 。

递归终止条件：
当越过叶子节点时，返回高度 0 ；
当左（右）子树高度 left== -1 时，代表此子树的 左（右）子树 不是平衡树，因此直接返回 −1


时间复杂度 O(N)： N 为树的节点数；最差情况下，需要递归遍历树的所有节点。
空间复杂度 O(N)： 最差情况下（树退化为链表时），系统递归需要使用 O(N) 的栈空间。
"""