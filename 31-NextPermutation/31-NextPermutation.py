# Last updated: 9/3/2026, 2:08:47 PM
1class Solution:
2    def solveSudoku(self, board: List[List[str]]) -> None:
3        """
4        Do not return anything, modify board in-place instead.
5        """
6        rows = [set() for _ in range(9)]
7        cols = [set() for _ in range(9)]
8        boxes = [set() for _ in range(9)]
9        empty = []
10
11        for r in range(9):
12            for c in range(9):
13                val = board[r][c]
14                if val != '.':
15                    rows[r].add(val)
16                    cols[c].add(val)
17                    boxes[(r // 3) * 3 + (c // 3)].add(val)
18                else:
19                    empty.append((r, c))
20
21        def backtrack(index):
22            if index == len(empty):
23                return True
24
25            r, c = empty[index]
26            box_idx = (r // 3) * 3 + (c // 3)
27
28            for char in "123456789":
29                if char not in rows[r] and char not in cols[c] and char not in boxes[box_idx]:
30                    board[r][c] = char
31                    rows[r].add(char)
32                    cols[c].add(char)
33                    boxes[box_idx].add(char)
34
35                    if backtrack(index + 1):
36                        return True
37
38                    board[r][c] = '.'
39                    rows[r].remove(char)
40                    cols[c].remove(char)
41                    boxes[box_idx].remove(char)
42
43            return False
44
45        backtrack(0)