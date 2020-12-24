# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return []
        
        mid = len(nums)//2 # 因为mid的值是适中的，作为父节点或者根节点很合适
        node = TreeNode(nums[mid]) # 将中间的值设为树的节点

        left = nums[:mid]
        right = nums[mid+1:]

        node.left = self.sortedArrayToBST(left) # 左节点
        node.right = self.sortedArrayToBST(right) # 右节点
        
        return node

"""
题目中 [-10,-3,0,5,9] 其实就是中序遍历得到的结果 左中右

二叉搜索树（Binary Search Tree）是指一棵空树或具有如下性质的二叉树：

1.若任意节点的 *左子树* 不空，则左子树上所有节点的值均 *小于* 它的根节点的值
2.若任意节点的 *右子树* 不空，则右子树上所有节点的值均 *大于* 它的根节点的值
3.任意节点的左、右子树也分别为二叉搜索树
4.没有键值相等的节点

基于以上性质，我们可以得出一个二叉搜索树的特性：二叉搜索树的中序遍历结果为递增序列。
那么现在题目给了我们一个递增序列，要求我们构造一棵二叉搜索树，就是要我们实现这一特性的逆过程。

还记得什么是中序遍历吗？中序遍历的顺序为：左节点 -> 根节点 -> 右节点。这个遍历过程可以使用递归非常直观地进行表示。
构造一棵树的过程可以拆分成无数个这样的子问题：构造树的每个节点以及节点之间的关系。对于每个节点来说，都需要：

1.选取节点
2.构造该节点的左子树
3.构造该节点的右子树

因题目要求构造一棵「高度平衡」的树，所以我们在选取节点时选择数组的 *中点* 作为根节点，以此来保证平衡性。


时间复杂度：O(n)，其中 n 是数组的长度。每个数字只访问一次。
空间复杂度：O(logn)，其中 n 是数组的长度。空间复杂度不考虑返回值，因此空间复杂度主要取决于递归栈的深度，递归栈的深度是O(logn)。
"""