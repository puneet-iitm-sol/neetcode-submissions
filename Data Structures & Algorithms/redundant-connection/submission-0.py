class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        n = len(edges)

        par = list(range(n + 1))
        rank = [0] * (n + 1)

        def find(x):
            if par[x] != x:
                par[x] = find(par[x])
            return par[x]

        def union(a, b):
            x = find(a)
            y = find(b)

            if x == y:
                return False

            if rank[x] > rank[y]:
                par[y] = x
            elif rank[x] < rank[y]:
                par[x] = y
            else:
                par[y] = x
                rank[x] += 1

            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]