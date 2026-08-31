# Last updated: 8/31/2026, 4:21:32 PM
1class Solution:
2    def threeSumClosest(self, nums: list[int], target: int) -> int:
3        nums.sort()
4        closest_sum = float('inf')
5        
6        for i in range(len(nums) - 2):
7            left = i + 1
8            right = len(nums) - 1
9            
10            while left < right:
11                current_sum = nums[i] + nums[left] + nums[right]
12                
13                if abs(target - current_sum) < abs(target - closest_sum):
14                    closest_sum = current_sum
15                    
16                if current_sum < target:
17                    left += 1
18                elif current_sum > target:
19                    right -= 1
20                else:
21                    return current_sum
22                    
23        return closest_sum