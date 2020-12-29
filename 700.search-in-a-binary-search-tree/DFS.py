# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root: #如果为空，直接pass
            pass
        else:
            if root.val == val: #如果等于目标值，返回该结点
                return root
            elif root.val >val: #大于目标值，搜索左子树
                return self.searchBST(root.left,val)
            else:    #小于目标值，搜索右子树
                return self.searchBST(root.right,val)
        
        return None #没找到，返回None
