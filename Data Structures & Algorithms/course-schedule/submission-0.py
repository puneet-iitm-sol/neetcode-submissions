class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = [-1]*numCourses
        adj = [[] for _ in range(numCourses)]
        for u,v in prerequisites:
            adj[u].append(v)
        def dfs(node,adj,visited):
            if visited[node] == 1:
                return False
            if visited[node] == 2:
                return True
            visited[node] = 1
            for adjnode in adj[node]:
                if not dfs(adjnode,adj,visited):
                    return False
            visited[node] = 2
            return True
        for i in range(numCourses):
            if not dfs(i,adj,visited):
                return False
        return True

        