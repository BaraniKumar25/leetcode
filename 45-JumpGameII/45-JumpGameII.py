# Last updated: 9/3/2026, 2:25:49 PM
1class Solution:
2    def generateMatrix(self, n: int) -> List[List[int]]:
3        matrix = [[0] * n for _ in range(n)]
4        top, bottom = 0, n - 1
5        left, right = 0, n - 1
6        num = 1
7
8        while top <= bottom and left <= right:
9            for col in range(left, right + 1):
10                matrix[top][col] = num
11                num += 1
12            top += 1
13
14            for row in range(top, bottom + 1):
15                matrix[row][right] = num
16                num += 1
17            right -= 1
18
19            if top <= bottom:
20                for col in range(right, left - 1, -1):
21                    matrix[bottom][col] = num
22                    num += 1
23                bottom -= 1
24
25            if left <= right:
26                for row in range(bottom, top - 1, -1):
27                    matrix[row][left] = num
28                    num += 1
29                left += 1
30
31        return matrix