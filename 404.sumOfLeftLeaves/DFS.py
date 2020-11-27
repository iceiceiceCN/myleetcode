# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.ans = 0

        def dfs(root):
            if root.left:
                if not root.left.left and not root.left.right:
                    self.ans += root.left.val
                else:
                    dfs(root.left)
            
            if root.right:
                dfs(root.right)
            
            return self.ans
        
        return dfs(root)

"""
self变量的用法！
题目的要求是要找到所有的左叶子之和，那么首先先考虑什么是叶子节点。
1.当二叉树中一个节点既没有左子节点，又没有右子节点的时候，就是叶子节点，因此，如果这个节点称为 node, 那么它应该满足 not node.left and not node.right。

2.然后需要考虑什么是左叶子节点，那么就要根据这个叶子节点的父节点来进行判断，如果这个叶子节点是父节点的左子节点，那么就满足条件，加到最终的和中。这时候把父节点命名为 node, 如果 if node.left 为真，表示该是父节点的左子节点。
相应地，这时候把1中的判断条件中的 node 替换为 node.left

3.最后，递归深搜每一个节点，如果满足条件，就加入和中，如果节点为空，就返回。
"""