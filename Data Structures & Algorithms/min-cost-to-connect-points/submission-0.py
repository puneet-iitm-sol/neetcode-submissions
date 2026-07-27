import heapq

class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)

        adj = [[] for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

                adj[i].append((j, dist))
                adj[j].append((i, dist))

        vis = [0] * n
        pq = [(0, 0)]
        ans = 0

        while pq:
            wt, node = heapq.heappop(pq)

            if vis[node]:
                continue

            vis[node] = 1
            ans += wt

            for adjNode, edgeWt in adj[node]:
                if not vis[adjNode]:
                    heapq.heappush(pq, (edgeWt, adjNode))

        return ans