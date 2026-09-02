class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # def dfs(node):
        #     if node in visited:
        #         return
        #     visited.add(node)
        #     for nei in graph[node]:
        #         dfs(nei)

        # graph = {i:[] for i in range(n)}
        # visited = set()
        # for a,b in edges:

        #     graph[a].append(b)
        #     graph[b].append(a)
        
        # component = 0
        # for node in range(n):
        #     if node not in visited:
        #         dfs(node)
        #         component += 1
        # return component
        par = [i for i in range(n)]
        rank = [1] * n
        def find(n):
            if par[n] != n:
                par[n] = find(par[n])
            return par[n]

        def union(n1,n2):
            p1,p2 = find(n1), find(n2)
            if p1 == p2:
                return 0
            if p1 > p2:
                par[p2] = p1
                rank[p1] += 1
            elif p2 > p1:
                par[p1] = p2
                rank[p2] =+ 1
            return 1
        component = n
        for n1,n2 in edges:
            component -= union(n1,n2)
        return component

        
