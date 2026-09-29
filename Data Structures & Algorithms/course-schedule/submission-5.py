from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[a].append(b)              # a needs b

        state = [0] * numCourses            # 0 = unvisited, 1 = visiting, 2 = done

        def dfs(course):
            if state[course] == 1:          # already on the current path: cycle
                return False
            if state[course] == 2:          # already checked, no cycle below it
                return True
            state[course] = 1               # entering this course
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            state[course] = 2               # every prerequisite checked out
            return True

        return all(dfs(c) for c in range(numCourses))