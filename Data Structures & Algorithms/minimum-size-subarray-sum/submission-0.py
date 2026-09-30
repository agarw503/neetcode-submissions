class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left  = 0
        cur_sum = 0
        min_len = n + 1 

        for right in range(n):
            cur_sum += nums[right] #adding to my sum

            while cur_sum >= target:
                min_len = min(min_len, right - left +1) # removing

                cur_sum -= nums[left]
                left += 1

        return 0 if min_len == n+1 else min_len


        