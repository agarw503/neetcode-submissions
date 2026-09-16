class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)          # O(1) lookups, and dedupes
        longest = 0

        for n in num_set:
            # only start a walk if n is the START of a sequence
            if n - 1 not in num_set:
                length = 1
                current = n
                while current + 1 in num_set:   # walk upward
                    current += 1
                    length += 1
                longest = max(longest, length)

        return longest