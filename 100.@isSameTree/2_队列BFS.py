# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        elif not p or not q:
            return False
        import collections
        
        queue1 = collections.deque([p])
        queue2 = collections.deque([q])

        while queue1 and queue2:
            node1 = queue1.popleft()
            node2 = queue2.popleft()

            if node1.val != node2.val:
                return False
            
            left1, right1 = node1.left, node1.right
            left2, right2 = node2.left, node2.right

            if (not left1) ^ (not left2):  # 只能一个为空（相异为真）
                return False
            if (not right1) ^ (not right2):
                return False
            """或者这么写
            if (not left1 and left2) or (not left2 and left1):
                return False
            if (not right1 and right2) or (not right2 and right1):
                return False
            """
            """
            if not left1 and not left2:
                pass
            elif not left1 or not left2:
                return False
            if not right1 and not right2:
                pass
            elif not right1 or not right2:
                return False
            """
            
            if left1:
                queue1.append(left1)
            if left2:
                queue2.append(left2)
            if right1:
                queue1.append(right1)
            if right2:
                queue2.append(right2)

        return not queue1 and not queue2

"""
方法二：广度优先搜索
也可以通过广度优先搜索判断两个二叉树是否相同。

同样首先判断两个二叉树是否为空，如果两个二叉树都不为空，则从两个二叉树的根节点开始广度优先搜索。
使用两个队列分别存储两个二叉树的节点。初始时将两个二叉树的根节点分别加入两个队列。每次从两个队列各取出一个节点，进行如下比较操作。

比较两个节点的值，如果两个节点的值不相同则两个二叉树一定不同；
如果两个节点的值相同，则判断两个节点的子节点是否为空，如果*只有*一个节点的左子节点为空，或者*只有*一个节点的右子节点为空，则两个二叉树的结构不同，因此两个二叉树一定不同；
如果两个节点的子节点的结构相同，则将两个节点的非空子节点分别加入两个队列，子节点加入队列时需要注意顺序，如果左右子节点都不为空，则先加入*左子节点，后加入右子节点*。

如果搜索结束时两个队列同时为空，则两个二叉树相同。如果只有一个队列为空，则两个二叉树的结构不同，因此两个二叉树不同。

时间复杂度：O(min(m,n))，其中 m 和 n 分别是两个二叉树的节点数。对两个二叉树同时进行广度优先搜索，只有当两个二叉树中的对应节点都不为空时才会访问到该节点，因此被访问到的节点数不会超过较小的二叉树的节点数。
空间复杂度：O(min(m,n))，其中 m 和 n 分别是两个二叉树的节点数。空间复杂度取决于队列中的元素个数，队列中的元素个数不会超过较小的二叉树的节点数。

"""