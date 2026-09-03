# Last updated: 9/3/2026, 2:48:56 PM
1class Solution:
2    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
3        if not obstacleGrid or obstacleGrid[0][0] == 1:
4            return 0
5
6        m, n = len(obstacleGrid), len(obstacleGrid[0])
7        dp = [0] * n
8        dp[0] = 1
9
10        for r in range(m):
11            for c in range(n):
12                if obstacleGrid[r][c] == 1:
13                    dp[c] = 0
14                elif c > 0:
15                    dp[c] += dp[c - 1]
16
17        return dp[-1]