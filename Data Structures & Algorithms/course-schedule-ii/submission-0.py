class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        visited = [-1] * numCourses
        adj = [[] for _ in range(numCourses)]

        for u, v in prerequisites:
            adj[v].append(u)

        stack = []

        def dfs(node):
            if visited[node] == 1:
                return False

            if visited[node] == 2:
                return True

            visited[node] = 1

            for nei in adj[node]:
                if not dfs(nei):
                    return False

            visited[node] = 2
            stack.append(node)

            return True

        for i in range(numCourses):
            if visited[i] == -1:
                if not dfs(i):
                    return []

        stack.reverse()
        return stack