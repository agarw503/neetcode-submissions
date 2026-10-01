import heapq
from math import inf
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Build adjacency list: node -> list of (neighbor, weight)
        graph = [[] for _ in range(n + 1)]
        for u, v, w in times:
            graph[u].append((v, w))

        # dist[i] = shortest known time from k to node i
        dist = [inf] * (n + 1)
        dist[k] = 0

        # Min-heap of (time, node)
        heap = [(0, k)]
        visited = [False] * (n + 1)

        while heap:
            d, u = heapq.heappop(heap)
            if visited[u]:
                continue
            visited[u] = True
            for v, w in graph[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(heap, (nd, v))

        # If any node is still unreachable, signal can't reach everyone
        max_delay = max(dist[1:])
        return -1 if max_delay == inf else max_delay