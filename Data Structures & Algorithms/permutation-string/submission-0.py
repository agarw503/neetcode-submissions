class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)

        if n1 > n2:
            return False 
        count = Counter(s1)

        for i in range(n2 - n1 +1):
            window = s2[i:i+n1]
            if Counter(window) == count:
                return True
        return False



        