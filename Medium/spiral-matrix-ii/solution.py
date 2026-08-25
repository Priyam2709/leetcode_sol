class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        r, c, di = 0, 0, 0
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        
        for val in range(1, n * n + 1):
            matrix[r][c] = val
            nr, nc = r + dr[di], c + dc[di]
            if not (0 <= nr < n and 0 <= nc < n and matrix[nr][nc] == 0):
                di = (di + 1) % 4
            r += dr[di]
            c += dc[di]
            
        return matrix