# Last updated: 8/24/2026, 8:50:32 AM
1class Solution:
2
3  def maxDepth(self, root: Optional[TreeNode]) -> int:
4    if not root:
5      return 0
6
7    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))