# Last updated: 8/24/2026, 8:57:51 AM
1class Solution:
2
3  def maxPathSum(self, root: Optional[TreeNode]) -> int:
4    max_sum = float('-inf')
5
6    def get_max_gain(node):
7      nonlocal max_sum
8      if not node:
9        return 0
10
11      left_gain = max(get_max_gain(node.left), 0)
12      right_gain = max(get_max_gain(node.right), 0)
13
14      current_path_sum = node.val + left_gain + right_gain
15      max_sum = max(max_sum, current_path_sum)
16
17      return node.val + max(left_gain, right_gain)
18
19    get_max_gain(root)
20    return max_sum