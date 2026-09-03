# Last updated: 9/3/2026, 2:10:59 PM
1class Solution:
2    def firstMissingPositive(self, nums: List[int]) -> int:
3        n = len(nums)
4
5        for i in range(n):
6            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
7                correct_idx = nums[i] - 1
8                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
9
10        for i in range(n):
11            if nums[i] != i + 1:
12                return i + 1
13
14        return n + 1