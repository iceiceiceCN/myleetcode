# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not inorder or not preorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:mid+1],inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])

        return root


"""
由于前序遍历的顺序是：中 - 左 - 右
中序遍历的顺序是：    左 - 中 - 右
此时可以发现【中-左】与【左-中】的规律
我们可以通过前序遍历的第一个元素来确定中序遍历中的 左子树 和 右子树
前序遍历中的[0]就是根节点；  [1:mid+1] 就是 左子树；[:mid]就是 右子树
中序遍历中的[mid]就是根节点；[:mid]就是 左子树；    [mid+1:]就是 右子树
以此进行递归

例如在例题中：

前序遍历 preorder = [3,9,20,15,7]

中序遍历 inorder = [9,3,15,20,7]

preorder 的第一个元素 3 是整棵树的根节点。
inorder 中 3 的左侧 [9] 是树的左子树，3 的右侧 [15, 20, 7] 构成了树的右子树。

所以构建二叉树的问题本质上就是：

    找到各个子树的根节点 root
    构建该根节点的左子树
    构建该根节点的右子树

"""