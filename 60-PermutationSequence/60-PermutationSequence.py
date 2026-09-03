# Last updated: 9/3/2026, 2:43:24 PM
1import math
2
3class Solution:
4    def uniquePaths(self, m: int, n: int) -> int:
5        return math.comb(m + n - 2, m - 1)