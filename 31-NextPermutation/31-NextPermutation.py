# Last updated: 9/3/2026, 2:10:13 PM
1class Solution:
2    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
3        candidates.sort()
4        res = []
5
6        def backtrack(start, current_combination, current_sum):
7            if current_sum == target:
8                res.append(list(current_combination))
9                return
10            if current_sum > target:
11                return
12
13            for i in range(start, len(candidates)):
14                if i > start and candidates[i] == candidates[i - 1]:
15                    continue
16                
17                current_combination.append(candidates[i])
18                backtrack(i + 1, current_combination, current_sum + candidates[i])
19                current_combination.pop()
20
21        backtrack(0, [], 0)
22        return res