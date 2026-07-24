from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        fresh = 0
        t = 0 
        pq = deque([])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    pq.append((i,j))
                if grid[i][j] == 1:
                    fresh +=1
        dirc = [(1,0),(-1,0),(0,1),(0,-1)]
        while pq and fresh:
            for _ in range(len(pq)):
                y, x = pq.popleft()

                for a, b in dirc:
                    dy = y + a
                    dx = x + b

                    if dy < 0 or dy >= n or dx < 0 or dx >= m:
                        continue

                    if grid[dy][dx] == 1:
                        grid[dy][dx] = 2
                        fresh -= 1
                        pq.append((dy, dx))

            t += 1
        if fresh:
            return -1
        return t
                


                


        