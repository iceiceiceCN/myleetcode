# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        def dfs(root, level):
            if not root:
                return

            if level < len(totals): # 计数器判断，如果小于len(totals)，说明该level不是新一层
                totals[level] += root.val
                counts[level] += 1

            else: # 如果不小于len(totals)，说明该level是新一层，直接在totals counts后面新增数组
                totals.append(root.val)
                counts.append(1)

            dfs(root.left, level+1) # level+1表明进入下一层了
            dfs(root.right, level+1)

        totals = list()
        counts = list()
        dfs(root, 0)
        return [total / count for total, count in zip(totals, counts)]
