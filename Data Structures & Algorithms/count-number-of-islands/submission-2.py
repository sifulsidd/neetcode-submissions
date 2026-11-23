class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        ROWS, COLS = len(grid), len(grid[0])
        
        def dfs(r, c, visit):
            if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == "0" or (r,c) in visit:
                return 
            
            visit.add((r,c))
            dfs(r + 1, c, visit)
            dfs(r - 1, c, visit)
            dfs(r, c + 1, visit)
            dfs(r, c - 1, visit)
            return 1 
        
        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "0" or (r, c) in visit:
                    continue
                islands += dfs(r, c, visit)
        return islands
                            
