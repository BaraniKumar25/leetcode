# Last updated: 9/3/2026, 2:18:54 PM
1class Solution:
2    def permute(self, nums: List[int]) -> List[List[int]]:
3        res = []
4
5        def backtrack(first=0):
6            if first == len(nums):
7                res.append(nums[:])
8                return
9            for i in range(first, len(nums)):
10                nums[first], nums[i] = nums[i], nums[first]
11                backtrack(first + 1)
12                nums[first], nums[i] = nums[i], nums[first]
13
14        backtrack()
15        return res