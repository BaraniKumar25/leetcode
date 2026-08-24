# Last updated: 8/24/2026, 8:57:29 AM
1class Solution:
2
3  def sumNumbers(self, root: Optional[TreeNode]) -> int:
4    def dfs(node, current_sum):
5      if not node:
6        return 0
7
8      current_sum = current_sum * 10 + node.val
9
10      if not node.left and not node.right:
11        return current_sum
12
13      return dfs(node.left, current_sum) + dfs(node.right, current_sum)
14
15    return dfs(root, 0)