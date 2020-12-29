# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if not root:
            return None

        # 因为是二叉搜索树,节点.left < 节点 < 节点.right
        # 如果数字比high大,就把右节点全部裁掉.
        # 裁掉之后,继续看左节点的剪裁情况
        if root.val > high:
            return self.trimBST(root.left, low, high)

        # 节点数字比low小,就把左节点全部裁掉.
        # 裁掉之后,继续看右节点的剪裁情况
        elif root.val < low:
            return self.trimBST(root.right, low, high)

        # 如果数字在区间内,就去裁剪左右子节点.
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)

        return root
