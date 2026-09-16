class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for c in s:
            if c.isalnum():          # keep only letters and digits
                cleaned += c.lower() # normalize case
        return cleaned == cleaned[::-1]   # compare to its reverse