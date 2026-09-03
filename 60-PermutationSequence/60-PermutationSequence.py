# Last updated: 9/3/2026, 2:49:25 PM
1class Solution:
2    def minPathSum(self, grid: List[List[int]]) -> int:
3        m, n = len(grid), len(grid[0])
4
5        dp = [float("inf")] * n
6        dp[0] = 0
7
8        for r in range(m):
9            dp[0] += grid[r][0]
10            for c in range(1, n):
11                dp[c] = min(dp[c], dp[c - 1]) + grid[r][c]
12
13        return dp[-1]