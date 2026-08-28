# Last updated: 8/28/2026, 11:10:49 AM
1class Solution:
2    def convert(self, s: str, numRows: int) -> str:
3        if numRows == 1 or numRows >= len(s):
4            return s
5        
6        rows = [''] * numRows
7        current_row = 0
8        going_down = False
9        
10        for char in s:
11            rows[current_row] += char
12            if current_row == 0 or current_row == numRows - 1:
13                going_down = not going_down
14            current_row += 1 if going_down else -1
15            
16        return ''.join(rows)