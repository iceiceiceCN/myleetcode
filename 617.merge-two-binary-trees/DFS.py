from TreeNodeTest import *

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:

        def dfs(r1, r2):
            if not r1 or not r2:
                return r1 if r1 else r2

            r1.val = r1.val + r2.val
            r1.left = dfs(r1.left, r2.left)
            r1.right = dfs(r1.right, r2.right)
            return r1
            
        return dfs(t1, t2)

if __name__ == "__main__":
    data = [1, 3, 2, 5]
    data2 = [2, 1, 3, None, 4, None, 7]
    pNode = generate_tree(data)
    pNode1 = generate_tree(data2)
    S = Solution()
    Sa = S.mergeTrees(pNode, pNode1)
    bfs(Sa)
