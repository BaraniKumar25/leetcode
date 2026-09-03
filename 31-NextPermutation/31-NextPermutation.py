# Last updated: 9/3/2026, 2:09:11 PM
1class Solution:
2    def countAndSay(self, n: int) -> str:
3        s = "1"
4        for _ in range(n - 1):
5            next_s = []
6            i = 0
7            while i < len(s):
8                count = 1
9                while i + 1 < len(s) and s[i] == s[i + 1]:
10                    count += 1
11                    i += 1
12                next_s.append(str(count))
13                next_s.append(s[i])
14                i += 1
15            s = "".join(next_s)
16        return s