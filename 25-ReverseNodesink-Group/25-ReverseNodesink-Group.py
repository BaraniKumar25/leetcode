# Last updated: 8/24/2026, 8:51:41 AM
1class Solution:
2
3  def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
4    if not root:
5      return None
6
7    root.left, root.right = root.right, root.left
8
9    self.invertTree(root.left)
10    self.invertTree(root.right)
11
12    return root