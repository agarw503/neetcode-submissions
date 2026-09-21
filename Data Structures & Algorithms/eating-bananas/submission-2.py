class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l , r = 1, max(piles)
        res = r
        while l <= r:
            mid = (l+r) // 2
            ttime = 0
            for p in piles:
                ttime += math.ceil(p / mid)
            if ttime <= h:
                res = mid
                r = mid -1 
            else:
                l = mid +1
        return res



        