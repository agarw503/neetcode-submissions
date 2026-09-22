class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        
        for i, temp in enumerate (temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prevday = stack.pop()
                result[prevday] = i - prevday
            stack.append(i)
        return result
