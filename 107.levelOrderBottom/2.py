class Solution(object):
    def levelOrderBottom(self, root):
        if not root:
            return []
        queue = [root]
        # 改用双端队列实现，每次都插入到第一位
        res = collections.deque()
        while queue:
            size = len(queue)
            tmp = []
            for _ in xrange(size):
                node = queue.pop(0)
                tmp.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # 每次插入到第一位，这样自带了翻转的功能       
            res.appendleft(tmp)
        return list(res)