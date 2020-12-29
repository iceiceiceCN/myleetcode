# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        def helper(node, val):
            if not node:
                return -1

            # 如果找到该节点的值大于根节点的值，则找到第二大的值的候选值
            if node.val > val:
                return node.val

            # 如果该节点不是的话，则找左子树和右子树
            left = helper(node.left, val)
            right = helper(node.right, val)
            
            # 如果左子树或者右子树为空，则返回另一边的子树
            if left < 0:
                return right
            if right < 0:
                return left
            
            # 如果左子树和右子树都找到了在其子树中最小的值，则比较一下哪个更小
            return min(left,right)
            
        return helper(root,root.val)
