class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_l, res_len = 0,0

        for i in range(len(s)):
            for l, r in ((i,i), (i,i+1)):
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    if r - l + 1 > res_len:
                        res_l, res_len  =l, r - l + 1
                    l -= 1
                    r += 1
        return s[res_l: res_l +res_len]