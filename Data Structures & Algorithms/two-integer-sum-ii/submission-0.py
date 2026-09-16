class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]   # +1 because the answer is 1-indexed
            elif total > target:
                right -= 1                      # too big → shrink from the right
            else:
                left += 1                       # too small → grow from the left
        return []

        