from TreeNodeTest import *

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
    # 如果 t1和t2中，只要有一个是null，函数就直接返回
        if not (t1 and t2):
            return t2 if not t1 else t1

        queue = [(t1, t2)]
        while queue:
            r1, r2 = queue.pop(0)

            r1.val += r2.val

            # 如果r1和r2的左子树都不为空，就放到队列中
            # 如果r1的左子树为空，就把r2的左子树挂到r1的左子树上
            # 因为是以 r1 为准，也就是把r1、r2的内容都合并到r1上，最后返回r1；如果r1的不空，但是r2是空的，相当于什么都不做，也就不用判断了 只要判断r1是空的，r2不空就可以了，这时候把r2赋给r1即可
            if r1.left and r2.left:
                queue.append((r1.left, r2.left))
            elif not r1.left:
                r1.left = r2.left
            # 对于右子树也是一样的
            if r1.right and r2.right:
                queue.append((r1.right, r2.right))
            elif not r1.right:
                r1.right = r2.right # 会把r2的整个右子树都接到r1上去
                
        return t1

if __name__ == "__main__":
    data = [1, 2, None, 3, None, 4, None]
    data2 = [1, None, 2, None, 3, None, 4]
    pNode = generate_tree(data)
    pNode1 = generate_tree(data2)
    S = Solution()
    Sa = S.mergeTrees(pNode, pNode1)
    bfs(Sa)
