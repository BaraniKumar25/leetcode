# Last updated: 9/3/2026, 2:26:12 PM
1import math
2
3class Solution:
4    def getPermutation(self, n: int, k: int) -> str:
5        numbers = [str(i) for i in range(1, n + 1)]
6        k -= 1
7        res = []
8
9        for i in range(n - 1, -1, -1):
10            fact = math.factorial(i)
11            index = k // fact
12            res.append(numbers.pop(index))
13            k %= fact
14
15        return "".join(res)