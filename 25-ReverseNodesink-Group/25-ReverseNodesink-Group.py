# Last updated: 8/24/2026, 8:51:15 AM
1class Solution:
2
3  def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
4    if not p and not q:
5      return True
6    if not p or not q or p.val != q.val:
7      return False
8
9    return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)