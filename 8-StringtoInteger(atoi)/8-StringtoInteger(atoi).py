# Last updated: 8/31/2026, 3:21:06 PM
1class Solution:
2    def isPalindrome(self, x: int) -> bool:
3        s = str(x)
4        return s == s[::-1]