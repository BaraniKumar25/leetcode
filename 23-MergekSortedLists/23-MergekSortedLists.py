# Last updated: 9/3/2026, 2:03:40 PM
1class Solution:
2    def nextPermutation(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        i = len(nums) - 2
7        # Find the first decreasing element from the right
8        while i >= 0 and nums[i] >= nums[i + 1]:
9            i -= 1
10
11        if i >= 0:
12            # Find the element just larger than nums[i] from the right
13            j = len(nums) - 1
14            while nums[j] <= nums[i]:
15                j -= 1
16            # Swap them
17            nums[i], nums[j] = nums[j], nums[i]
18
19        # Reverse the suffix starting at index i + 1
20        left, right = i + 1, len(nums) - 1
21        while left < right:
22            nums[left], nums[right] = nums[right], nums[left]
23            left += 1
24            right -= 1