from collections import deque
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        maxArea = 0

        def bfs(r, c):
            q = deque()
            visit.add((r, c))
            q.append((r, c))
            a = 1                                   
            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr in range(rows) and nc in range(cols) and
                            (nr, nc) not in visit and grid[nr][nc] == 1):
                        q.append((nr, nc))
                        visit.add((nr, nc))
                        a += 1
            return a

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    maxArea = max(maxArea, bfs(r, c))

        return maxArea