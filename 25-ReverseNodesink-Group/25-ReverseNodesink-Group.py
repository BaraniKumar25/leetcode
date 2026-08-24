# Last updated: 8/24/2026, 9:11:49 AM
1class Solution:
2
3  def lowestCommonAncestor(
4      self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'
5  ) -> 'TreeNode':
6    if not root or root == p or root == q:
7      return root
8
9    left = self.lowestCommonAncestor(root.left, p, q)
10    right = self.lowestCommonAncestor(root.right, p, q)
11
12    if left and right:
13      return root
14
15    return left if left else right