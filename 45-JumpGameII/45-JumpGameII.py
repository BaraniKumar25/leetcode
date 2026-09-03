# Last updated: 9/3/2026, 2:19:14 PM
1class Solution:
2    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
3        nums.sort()
4        res = []
5        used = [False] * len(nums)
6
7        def backtrack(path):
8            if len(path) == len(nums):
9                res.append(path[:])
10                return
11
12            for i in range(len(nums)):
13                if used[i]:
14                    continue
15                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
16                    continue
17
18                used[i] = True
19                path.append(nums[i])
20                backtrack(path)
21                path.pop()
22                used[i] = False
23
24        backtrack([])
25        return res