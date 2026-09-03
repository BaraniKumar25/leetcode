# Last updated: 9/3/2026, 1:59:18 PM
1class Solution:
2    def generateParenthesis(self, n: int) -> List[str]:
3        res = []
4
5        def backtrack(open_count, close_count, current_str):
6            if len(current_str) == 2 * n:
7                res.append(current_str)
8                return
9            
10            if open_count < n:
11                backtrack(open_count + 1, close_count, current_str + "(")
12                
13            if close_count < open_count:
14                backtrack(open_count, close_count + 1, current_str + ")")
15
16        backtrack(0, 0, "")
17        return res