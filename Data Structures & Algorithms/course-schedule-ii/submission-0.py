class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        for a,b in prerequisites:
            adj[b].append(a)
            in_degree [a] += 1

        queue = deque()
        for i in range(numCourses):
            if in_degree [i] == 0:
                queue.append(i)
        
        order = []

        while queue:
            course = queue.popleft()
            order.append(course)

            for nc in adj[course]:
                in_degree[nc] -= 1
                if in_degree[nc] == 0:
                    queue.append(nc)
        return order if len(order)  == numCourses else []