class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n - 1:
            return False
        
        graph = [[] for _ in range(n)]
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visit ={0}
        q = deque([0])
        while q:
            node = q.popleft()
            for nei in graph[node]:
                if nei not in visit:
                    visit.add(nei)
                    q.append(nei)
        return len(visit) == n
