# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        paths = []
        queue = [(root,'')]
        while queue:
            node ,path= queue.pop(0)
            path += str(node.val)
            if not node.left and not node.right:
                paths.append(path)
            else:
                if node.left:
                    queue.append((node.left,str(path)+"->"))
                if node.right:
                    queue.append((node.right,str(path)+"->"))
        
        return paths

"""
方法二：广度优先搜索
思路与算法

我们也可以用广度优先搜索来实现。我们维护一个队列，存储节点以及根到该节点的路径。
一开始这个队列里只有根节点。在每一步迭代中，我们取出队列中的首节点，如果它是叶子节点，则将它对应的路径加入到答案中。
如果它不是叶子节点，则将它的所有孩子节点加入到队列的末尾。
当队列为空时广度优先搜索结束，我们即能得到答案。

"""