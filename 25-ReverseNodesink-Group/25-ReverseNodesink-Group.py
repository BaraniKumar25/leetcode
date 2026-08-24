# Last updated: 8/24/2026, 8:57:11 AM
1class Solution:
2
3  def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
4    if not root:
5      return False
6
7    if not root.left and not root.right:
8      return targetSum == root.val
9
10    targetSum -= root.val
11
12    return self.hasPathSum(root.left, targetSum) or self.hasPathSum(
13        root.right, targetSum
14    )