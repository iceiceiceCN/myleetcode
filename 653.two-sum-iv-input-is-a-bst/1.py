# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def helper(root):
            if not root:
                return []

            return helper(root.left) + [root.val] + helper(root.right)

        alist = helper(root)
        left, right = 0, len(alist)-1
        while right > left:
            sum_ = alist[left] + alist[right]
            if sum_ == k:
                return True
            elif sum_ < k:
                left += 1
            elif sum_ > k:
                right -= 1
        
        return False


# BST的性质：中序遍历是升序数组
