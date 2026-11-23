class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        # bfs 
        queue = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in visit or grid[r][c] == "0":
                    continue
                queue.append((r,c))
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                while queue:
                    for i in range(len(queue)):
                        r, c = queue.popleft()
                        visit.add((r,c))
                        for dr, dc in directions:
                            nr = r + dr
                            nc = c + dc
                            if min(nr, nc) < 0 or (nr,nc) in visit or nr == ROWS or nc == COLS or grid[nr][nc] == "0":
                                continue 
                            queue.append((nr, nc))
                            visit.add((nr, nc))
                islands += 1
        return islands
                            
