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
        if not root:
            return True
        return (abs(self.depth(root.left)-self.depth(root.right)) <= 1 and
                self.isBalanced(root.left) and self.isBalanced(root.right))

    def depth(self, root):
        if not root:
            return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        def depth(root): # 得到二叉树深度模板
            if not root:
                return 0

            return max(depth(root.left), depth(root.right))+1

        return abs(depth(root.left) - depth(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)


"""
从顶至底：
思路是构造一个获取当前节点最大深度的方法 depth(root)，
通过比较此子树的左右子树的最大高度差abs(depth(root.left) - depth(root.right))，来判断此子树是否是二叉平衡树。
若树的所有子树都平衡时，此树才平衡。

算法流程：
isBalanced(root) ：判断树 root 是否平衡
特例处理： 若树根节点 root 为空，则直接返回 truetrue ；
返回值： 所有子树都需要满足平衡树性质，因此以下三者使用与逻辑 && 连接；
abs(self.depth(root.left) - self.depth(root.right)) <= 1 ：判断 当前子树 是否是平衡树；
self.isBalanced(root.left) ： 先序遍历递归，判断 当前子树的左子树 是否是平衡树；
self.isBalanced(root.right) ： 先序遍历递归，判断 当前子树的右子树 是否是平衡树；

depth(root) ： 计算树 root 的最大高度
终止条件： 当 root 为空，即越过叶子节点，则返回高度 0 ；
返回值： 返回左 / 右子树的最大高度加 1 。

复杂度分析：
时间复杂度 O(Nlog2 N)： 
最差情况下， isBalanced(root) 遍历树所有节点，占用 O(N) ；
判断每个节点的最大高度 depth(root) 需要遍历各子树的所有节点，树的节点数的复杂度为 O(log2 N) 。


空间复杂度 O(N)： 
最差情况下（树退化为链表时），系统递归需要使用 O(N) 的栈空间。


"""
