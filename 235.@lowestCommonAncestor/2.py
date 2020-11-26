# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        ans = root
        while True:
            if p.val > ans.val and q.val > ans.val:
                ans = ans.right
            if p.val < ans.val and q.val < ans.val:
                ans = ans.left
            else:
                break

        return ans
"""
方法二：一次遍历
根据二叉搜索树的特点，如果p,q都大于或者小于当前节点，说明他们在同一边子树中，所以再往下找，直到当前节点的值卡在p,q之间，那么就是公共父节点。
思路与算法

在方法一中，我们对从根节点开始，通过遍历找出到达节点 p 和 q 的路径，一共需要两次遍历。我们也可以考虑将这两个节点放在一起遍历。
整体的遍历过程与方法一中的类似：

我们从根节点开始遍历；
如果当前节点的值大于 p 和 q 的值，说明 p 和 q 应该在当前节点的左子树，因此将当前节点移动到它的左子节点；
如果当前节点的值小于 p 和 q 的值，说明 p 和 q 应该在当前节点的右子树，因此将当前节点移动到它的右子节点；
如果当前节点的值不满足上述两条要求，那么说明当前节点就是「分岔点」。此时，pp 和 qq 要么在当前节点的不同的子树中，要么其中一个就是当前节点。

可以发现，如果我们将这两个节点放在一起遍历，我们就省去了存储路径需要的空间。
"""