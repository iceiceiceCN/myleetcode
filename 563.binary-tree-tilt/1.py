# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 本题与求二叉树直径题目类似，
# 递归函数是求树的节点和
# 定义dfs函数求以某节点为根节点的树的节点总和，res+=坡度  即为总坡度
# 即res+=dfs(左子树)-dfs（右子树）的绝对值
# 而左子树之和加右子树之和加节点值为总树的和，巧妙复用了

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        res = 0

        def dfs(root):
            nonlocal res
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            res += abs(left-right)

            return root.val + left + right
            # 返回该节点与左右子树之和，叶节点返回的就是叶节点的val
        dfs(root)
        return res
