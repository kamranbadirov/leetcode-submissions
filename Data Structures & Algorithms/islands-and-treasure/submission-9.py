class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # this is a bfs problem, because we want to find the shortest distance between two points. 
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        INF = 2147483647
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
                if grid[r][c] == 2147483647:
                    grid[r][c] = INF

        while q:
            r,c = q.popleft()
            distance = 0
            for dr, dc in [[0,1], [0,-1], [1,0], [-1,0]]:
                nr,nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == INF:
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr,nc))
                
        