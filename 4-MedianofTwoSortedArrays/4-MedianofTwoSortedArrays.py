# Last updated: 8/28/2026, 11:10:09 AM
1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3        res = ""
4        for i in range(len(s)):
5            l, r = i, i
6            while l >= 0 and r < len(s) and s[l] == s[r]:
7                if (r - l + 1) > len(res):
8                    res = s[l:r + 1]
9                l -= 1
10                r += 1
11            l, r = i, i + 1
12            while l >= 0 and r < len(s) and s[l] == s[r]:
13                if (r - l + 1) > len(res):
14                    res = s[l:r + 1]
15                l -= 1
16                r += 1
17        return res