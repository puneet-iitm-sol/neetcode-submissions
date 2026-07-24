class Solution:
    def dfs(self,i,j,visited,grid):
        n = len(grid)
        m = len(grid[0])

        if 0 <= i < n and 0 <= j < m and grid[i][j] == 1 and not visited[i][j]:
            visited[i][j] = 1
            a = self.dfs(i+1,j,visited,grid)
            b = self.dfs(i,j+1,visited,grid)
            c = self.dfs(i-1,j,visited,grid)
            d = self.dfs(i,j-1,visited,grid)
            return 1 + a+b+c+d
        
        return 0            
        

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        max_area = 0
        visited = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not visited[i][j]:
                    area = self.dfs(i,j,visited,grid)
                    max_area = max(max_area, area)
        return max_area