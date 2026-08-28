# Last updated: 8/28/2026, 11:09:46 AM
1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3        res = ""
4        
5        for i in range(len(s)):
6            # Odd length palindromes (single character center)
7            l, r = i, i
8            while l >= 0 and r < len(s) and s[l] == s[r]:
9                if (r - l + 1) > len(res):
10                    res = s[l:r + 1]
11                l -= 1
12                r += 1
13            
14            # Even length palindromes (two character center)
15            l, r = i, i + 1
16            while l >= 0 and r < len(s) and s[l] == s[r]:
17                if (r - l + 1) > len(res):
18                    res = s[l:r + 1]
19                l -= 1
20                r += 1
21                
22        return res