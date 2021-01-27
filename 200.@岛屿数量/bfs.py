class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(grid, i, j):
            queue = [[i, j]]
            while queue:
                [i, j] = queue.pop(0)
                if 0 <= i <= len(grid)-1 and 0 <= j <= len(grid[0])-1 and grid[i][j] == '1':
                    grid[i][j] = '0'
                    queue += [[i + 1, j], [i - 1, j], [i, j - 1], [i, j + 1]]

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    bfs(grid,i,j)
                    count +=1
        
        return count

"""
思路二：广度优先遍历 BFS
主循环和思路一类似，不同点是在于搜索某岛屿边界的方法不同。
bfs 方法：
借用一个队列 queue，判断队列首部节点 (i, j) 是否未越界且为 1：
若是则置零（删除岛屿节点），并将此节点上下左右节点 (i+1,j),(i-1,j),(i,j+1),(i,j-1) 加入队列；
若不是则跳过此节点；
循环 pop 队列首节点，直到整个队列为空，此时已经遍历完此岛屿。

"""