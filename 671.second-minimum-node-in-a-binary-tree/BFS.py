# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root:
            return

        queue = [root]
        nums = set()

        while queue:
            node = queue.pop(0)
            nums.add(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        mins = min(nums)
        nums.remove(mins)

        return min(nums) if len(nums) > 0 else -1
