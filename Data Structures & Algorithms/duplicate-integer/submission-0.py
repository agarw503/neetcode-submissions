class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        exist = set()
        for items in nums:
            if items in exist:
                return True
            exist.add(items)
        return False