# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        dicts = {}

        # 使用DFS来整一遍
        def dfs(root):
            if not root:
                return
            if root.val not in dicts:
                dicts[root.val] = 1
            else:
                dicts[root.val] += 1
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        print(dicts)
        maxVal = max(dicts.values())
        ans = []
        for item, val in dicts.items():
            if val >= maxVal:
                ans.append(item)
        return ans
