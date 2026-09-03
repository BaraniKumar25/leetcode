# Last updated: 9/3/2026, 2:20:48 PM
1class Solution:
2    def totalNQueens(self, n: int) -> int:
3        cols = set()
4        pos_diag = set()  # (r + c)
5        neg_diag = set()  # (r - c)
6
7        def backtrack(r):
8            if r == n:
9                return 1
10
11            count = 0
12            for c in range(n):
13                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
14                    continue
15
16                cols.add(c)
17                pos_diag.add(r + c)
18                neg_diag.add(r - c)
19
20                count += backtrack(r + 1)
21
22                cols.remove(c)
23                pos_diag.remove(r + c)
24                neg_diag.remove(r - c)
25
26            return count
27
28        return backtrack(0)