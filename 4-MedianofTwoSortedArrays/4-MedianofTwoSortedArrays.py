# Last updated: 8/28/2026, 11:11:23 AM
1class Solution:
2    def reverse(self, x: int) -> int:
3        sign = -1 if x < 0 else 1
4        x_abs = abs(x)
5        
6        reversed_num = int(str(x_abs)[::-1]) * sign
7        
8        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
9            return 0
10            
11        return reversed_num