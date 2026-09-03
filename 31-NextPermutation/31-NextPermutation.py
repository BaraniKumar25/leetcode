# Last updated: 9/3/2026, 2:09:42 PM
1class Solution:
2    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
3        res = []
4
5        def backtrack(start, current_combination, current_sum):
6            if current_sum == target:
7                res.append(list(current_combination))
8                return
9            if current_sum > target:
10                return
11
12            for i in range(start, len(candidates)):
13                current_combination.append(candidates[i])
14                backtrack(i, current_combination, current_sum + candidates[i])
15                current_combination.pop()
16
17        backtrack(0, [], 0)
18        return res