class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        dic = {root:None}
        def dfs(node):
            if node:
                if node.left: 
                    dic[node.left] = node
                if node.right: 
                    dic[node.right] = node
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        l1, l2 = p, q
        while(l1!=l2):
            l1 = dic.get(l1, q)
            l2 = dic.get(l2, p)
        return l1 

"""
记公共祖先节点是A，整棵树的根节点为root， P、Q距离A的步数分别是：a、b步，A距离root距离是c步， 
那么P沿着父节点方向往上走a+c步就到达root节点，这时候让P再沿着Q到A的路径走b步，就停在A处，此时P的路程是a+c+b；
同样的方法，Q的路程是b+c+a。 
发现两者同时走到A，即判定条件 l1==l2时要跳出循环。
另外，如果a==b的话，那么P，Q不用完全走完就会相遇。

相当于找相同次数的祖先节点
"""