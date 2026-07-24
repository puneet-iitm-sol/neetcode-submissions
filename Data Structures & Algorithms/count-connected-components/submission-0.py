class Solution:
    def dfs(self,node,visited,adj):
        visited[node] = 1
        for adjnode in adj[node]:
            if visited[adjnode] == -1:
                self.dfs(adjnode,visited,adj)

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        c = 0
        visited = [-1]*n
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        for i in range(n):
            if visited[i] == -1:
                self.dfs(i,visited,adj)
                c+=1
        return c
        