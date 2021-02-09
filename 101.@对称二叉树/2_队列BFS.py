# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root or (not root.left and not root.right): # 没有根节点或者只有一个根节点，没有任何子树
            return True

        # 用队列保存节点
        queue = [root.left,root.right]

        while queue:
            # 从队列中取出两个节点，再比较这两个节点
            left = queue.pop(0) # 可以用pop(0)来实现popleft()
            right = queue.pop(0)

            # 如果两个节点都为空就继续循环，两者有一个为空就返回false
            if not left and not right:
                continue # 不能返回True，因为后面子树还需要继续比较，待全部比较完才能说明树对称
            if not left or not right:
                return False
            if left.val != right.val:
                return False

            # 将左节点的左孩子， 右节点的右孩子放入队列
            queue.append(left.left)
            queue.append(right.right)

            # 将左节点的右孩子，右节点的左孩子放入队列 # 其实谁前谁后没区别
            queue.append(left.right)
            queue.append(right.left)
        
        return not queue # 如果队列遍历完毕都为true 则为ture
        # return True