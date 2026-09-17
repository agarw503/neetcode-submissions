class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        left = 0
        longest = 0
        for k in range (len(s)):
            while s[k] in window:
                window.remove(s[left])
                left += 1
            window.add(s[k])
            longest = max(longest, k - left + 1)
        return longest
      