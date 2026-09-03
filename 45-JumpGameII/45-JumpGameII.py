# Last updated: 9/3/2026, 2:20:22 PM
1class Solution:
2    def solveNQueens(self, n: int) -> List[List[str]]:
3        res = []
4        cols = set()
5        pos_diag = set()  # (r + c)
6        neg_diag = set()  # (r - c)
7
8        board = [["."] * n for _ in range(n)]
9
10        def backtrack(r):
11            if r == n:
12                res.append(["".join(row) for row in board])
13                return
14
15            for c in range(n):
16                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
17                    continue
18
19                cols.add(c)
20                pos_diag.add(r + c)
21                neg_diag.add(r - c)
22                board[r][c] = "Q"
23
24                backtrack(r + 1)
25
26                cols.remove(c)
27                pos_diag.remove(r + c)
28                neg_diag.remove(r - c)
29                board[r][c] = "."
30
31        backtrack(0)
32        return res