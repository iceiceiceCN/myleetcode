# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        while root or stack:
            if root: # 如果存在节点就往左走
                stack.append(root)
                root = root.left

            else: # 如果不存在节点，则说明左边走到头了，开始出栈，然后转向右边的节点，之后继续往左走
                tmp = stack.pop()
                res.append(tmp.val)
                root = tmp.right
        
        return res