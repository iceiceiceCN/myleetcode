# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        queue = [(root,1)]
        while queue:
            node,depth = queue.pop(0)
            if not node.left and not node.right:
                return depth
            if node.left:
                queue.append((node.left,depth+1))
            if node.right:
                queue.append((node.right,depth+1))
            
        return 0

"""
方法二：广度优先搜索

同样，我们可以想到使用广度优先搜索的方法，遍历整棵树。
当我们找到一个叶子节点时，直接返回这个叶子节点的深度。
广度优先搜索的性质保证了最先搜索到的叶子节点的深度一定最小。

时间复杂度：O(N)，其中 N 是树的节点数。对每个节点访问一次。
空间复杂度：O(N)，其中 N 是树的节点数。空间复杂度主要取决于队列的开销，队列中的元素个数不会超过树的节点数。
"""