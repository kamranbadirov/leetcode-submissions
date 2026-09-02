class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)

        # Initialize graph and visited set
        graph = {i: [] for i in range(n)}
        visited = set()
        
        # Build the graph
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        # Count connected components
        components = 0
        for node in range(n):
            if node not in visited:
                dfs(node)
                components += 1
                
        return components

            
