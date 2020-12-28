# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        
        queue = [root]
        res = []

        while queue:
            num = len(queue)
            tmp = 0
            
            for _ in range(num):
                node = queue.pop(0)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

                tmp += node.val
                
            tmp /= num
            res.append(tmp)
            
        return res
            

