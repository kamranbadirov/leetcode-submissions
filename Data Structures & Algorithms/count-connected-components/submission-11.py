class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in graph[node]:
                dfs(nei)

        graph = {i:[] for i in range(n)}
        visited = set()
        for a,b in edges:

            graph[a].append(b)
            graph[b].append(a)
        
        component = 0
        for node in range(n):
            if node not in visited:
                dfs(node)
                component += 1
        return component
                
        
