# Last updated: 8/28/2026, 11:09:11 AM
1class Solution:
2    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
3        merged = sorted(nums1 + nums2)
4        n = len(merged)
5        mid = n // 2
6        
7        if n % 2 == 1:
8            return float(merged[mid])
9        else:
10            return (merged[mid - 1] + merged[mid]) / 2.0