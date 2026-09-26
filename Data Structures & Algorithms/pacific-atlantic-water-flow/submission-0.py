class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        def dfs (ocean):
            q = deque(ocean)
            seen = set(ocean)   
            while q:
                r,c = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if nr in range(rows) and nc in range(cols) and heights[nr][nc] >= heights[r][c] and (nr, nc) not in seen:
                        seen.add((nr,nc))
                        q.append((nr,nc))
            return seen
        
        pacific = [(r,0) for r in range (rows)] +[(0,c) for c in range (cols)]
        atlantic = [(rows- 1, c) for c in range(cols)] + [(r, cols - 1) for r in range(rows)]
        both = dfs(pacific) & dfs(atlantic)
        return [(r,c) for r,c in both]