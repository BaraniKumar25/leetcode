# Last updated: 9/3/2026, 2:03:09 PM
1class Solution:
2    def divide(self, dividend: int, divisor: int) -> int:
3        INT_MAX = 2**31 - 1
4        INT_MIN = -2**31
5
6        # Handle overflow case
7        if dividend == INT_MIN and divisor == -1:
8            return INT_MAX
9
10        # Determine the sign of the result
11        negative = (dividend < 0) ^ (divisor < 0)
12
13        # Work with positive values
14        a, b = abs(dividend), abs(divisor)
15        quotient = 0
16
17        # Bit shifting approach (exponential sub)
18        while a >= b:
19            temp = b
20            multiple = 1
21            while a >= (temp << 1):
22                temp <<= 1
23                multiple <<= 1
24            a -= temp
25            quotient += multiple
26
27        return -quotient if negative else quotient