class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if not left and not right:
            return  # 1.
        if not left:
            return right  # 3.
        if not right:
            return left  # 4.
        
        return root  # 2. if left and right:


# https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/236-er-cha-shu-de-zui-jin-gong-gong-zu-xian-hou-xu/
"""
1.  当 left 和 right 同时为空 ：说明 root 的左 / 右子树中都不包含p,q ，返回 null ；
2.  当 left 和 right 同时不为空 ：说明 p,q 分列在 root 的 异侧 （分别在 左 / 右子树），因此 root 为最近公共祖先，返回 root ；
3.  当 left 为空 ，right 不为空 p,q 都不在 root 的左子树中，直接返回 right 。具体可分为两种情况：
    1.  p,q 其中一个在 root 的 右子树 中，此时 right 指向 p（假设为 p ）；
    2.  p,q 两节点都在 root 的 右子树 中，此时的 right 指向 最近公共祖先节点 ；
4.  当 left 不为空 ， right 为空 ：与情况 3. 同理；

"""