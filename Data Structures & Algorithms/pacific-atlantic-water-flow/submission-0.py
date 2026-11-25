class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # start from r = 0 and c = 0 for pacific
        # stat from r = ROWS - 1 and c = COLS - 1 for atlantic 
        # go to cells of increasing or equal heights only 
        ROWS, COLS = len(heights), len(heights[0])
        atl = set()
        pac = set()


        def dfs(r, c, visit, prevHeight):
            if (min(r, c) < 0) or (r == ROWS) or (c == COLS) or ((r,c) in visit) or heights[r][c] < prevHeight:
                return 

            visit.add((r,c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])



        for c in range(COLS):
            # 0, c -> for pacific ocean because we know everything on top row is pacific
            dfs(0, c, pac, heights[0][c])
            # ROWS - 1, c -> for atlantic because we know everything on bottom row is atlant
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
        
        for r in range(ROWS):
            # column 0 means pacific
            dfs(r, 0, pac, heights[r][0])
            # columns COLS - 1 is atlantic
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in atl and (r,c) in pac:
                    res.append([r,c])
        return res