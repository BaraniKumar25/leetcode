# Last updated: 9/3/2026, 1:56:51 PM
1class Solution:
2    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
3        nums.sort()
4        n = len(nums)
5        res = []
6
7        for i in range(n - 3):
8            if i > 0 and nums[i] == nums[i - 1]:
9                continue
10            for j in range(i + 1, n - 2):
11                if j > i + 1 and nums[j] == nums[j - 1]:
12                    continue
13                left, right = j + 1, n - 1
14                while left < right:
15                    total = nums[i] + nums[j] + nums[left] + nums[right]
16                    if total == target:
17                        res.append([nums[i], nums[j], nums[left], nums[right]])
18                        while left < right and nums[left] == nums[left + 1]:
19                            left += 1
20                        while left < right and nums[right] == nums[right - 1]:
21                            right -= 1
22                        left += 1
23                        right -= 1
24                    elif total < target:
25                        left += 1
26                    else:
27                        right -= 1
28
29        return res