# Last updated: 9/3/2026, 2:15:39 PM
1class Solution:
2    def isMatch(self, s: str, p: str) -> bool:
3        s_ptr = p_ptr = 0
4        star_idx = s_tmp_idx = -1
5
6        while s_ptr < len(s):
7            if p_ptr < len(p) and (p[p_ptr] == '?' or p[p_ptr] == s[s_ptr]):
8                s_ptr += 1
9                p_ptr += 1
10            elif p_ptr < len(p) and p[p_ptr] == '*':
11                star_idx = p_ptr
12                s_tmp_idx = s_ptr
13                p_ptr += 1
14            elif star_idx != -1:
15                p_ptr = star_idx + 1
16                s_tmp_idx += 1
17                s_ptr = s_tmp_idx
18            else:
19                return False
20
21        while p_ptr < len(p) and p[p_ptr] == '*':
22            p_ptr += 1
23
24        return p_ptr == len(p)