import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dis = [float('inf')]*(n+1)
        dis[k] = 0
        pq = [(0,k)]
        adj = [[] for _ in range(n+1)]
        for u,v,w in times:
            adj[u].append((v,w))
        while pq:
            d,node = heapq.heappop(pq)
            if d>dis[node]:
                continue
            for adjnode,wt in adj[node]:
                if d + wt < dis[adjnode]:
                    dis[adjnode] = d + wt 
                    heapq.heappush(pq,(dis[adjnode],adjnode)) 
        if float('inf') in dis[1:]:
            return -1

        return max(dis[1:])

        