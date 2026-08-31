# Last updated: 8/31/2026, 3:20:42 PM
1class Solution:
2    def myAtoi(self, s: str) -> int:
3        s = s.lstrip()
4        if not s:
5            return 0
6
7        sign = 1
8        i = 0
9
10        if s[0] == '-':
11            sign = -1
12            i += 1
13        elif s[0] == '+':
14            i += 1
15
16        num = 0
17        while i < len(s) and s[i].isdigit():
18            num = num * 10 + int(s[i])
19            i += 1
20
21        num *= sign
22
23        INT_MIN = -2**31
24        INT_MAX = 2**31 - 1
25
26        if num < INT_MIN:
27            return INT_MIN
28        if num > INT_MAX:
29            return INT_MAX
30
31        return num