# Last updated: 9/3/2026, 2:19:53 PM
1class Solution:
2    def myPow(self, x: float, n: int) -> float:
3        if n < 0:
4            x = 1 / x
5            n = -n
6
7        res = 1.0
8        while n > 0:
9            if n % 2 == 1:
10                res *= x
11            x *= x
12            n //= 2
13
14        return res