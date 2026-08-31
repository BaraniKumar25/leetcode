# Last updated: 8/31/2026, 3:21:33 PM
1class Solution:
2    def isMatch(self, s: str, p: str) -> bool:
3        memo = {}
4
5        def dp(i, j):
6            if (i, j) in memo:
7                return memo[(i, j)]
8            
9            if j == len(p):
10                return i == len(s)
11
12            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')
13
14            if j + 1 < len(p) and p[j + 1] == '*':
15                ans = dp(i, j + 2) or (first_match and dp(i + 1, j))
16            else:
17                ans = first_match and dp(i + 1, j + 1)
18
19            memo[(i, j)] = ans
20            return ans
21
22        return dp(0, 0)