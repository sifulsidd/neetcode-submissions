class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        colorOfPosition = image[sr][sc]
        if colorOfPosition == color:    
            return image       
        queue = deque([[sr, sc]])
        image[sr][sc] = color
        while queue:
            for i in range(len(queue)):
                r , c = queue.popleft()
                
                directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
                for dr, dc in directions:
                    nr = r + dr 
                    nc = c + dc 
                    if min(nr, nc) < 0 or nr == ROWS or nc == COLS or image[nr][nc] != colorOfPosition:
                        continue 
                    image[nr][nc] = color
                    queue.append([nr, nc])
        return image