from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        if not heights:
            return []

        m = len(heights)
        n = len(heights[0])

        pacific = [[False] * n for _ in range(m)]
        atlantic = [[False] * n for _ in range(m)]

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(i, j, visited):
            visited[i][j] = True

            for dx, dy in directions:
                ni = i + dx
                nj = j + dy

                if (
                    0 <= ni < m and
                    0 <= nj < n and
                    not visited[ni][nj] and
                    heights[ni][nj] >= heights[i][j]
                ):
                    dfs(ni, nj, visited)

        # Pacific Ocean (Top row + Left column)
        for i in range(m):
            dfs(i, 0, pacific)

        for j in range(n):
            dfs(0, j, pacific)

        # Atlantic Ocean (Bottom row + Right column)
        for i in range(m):
            dfs(i, n - 1, atlantic)

        for j in range(n):
            dfs(m - 1, j, atlantic)

        ans = []

        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    ans.append([i, j])

        return ans