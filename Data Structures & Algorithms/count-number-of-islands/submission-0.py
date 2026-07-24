class Solution:
    def dfs(self,i,j,visited,grid):
        n = len(grid)
        m = len(grid[0])
        if 0 <= i < n and 0 <= j < m and grid[i][j] == "1" and not visited[i][j]:
            visited[i][j] = 1
            self.dfs(i+1,j,visited,grid)
            self.dfs(i,j+1,visited,grid)
            self.dfs(i-1,j,visited,grid)
            self.dfs(i,j-1,visited,grid)
        

    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        count  = 0
        visited = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and not visited[i][j]:
                    self.dfs(i,j,visited,grid)
                    count+=1
        return count