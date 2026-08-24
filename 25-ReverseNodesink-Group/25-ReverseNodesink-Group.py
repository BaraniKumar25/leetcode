# Last updated: 8/24/2026, 8:52:27 AM
1class Solution:
2
3  def isSymmetric(self, root: Optional[TreeNode]) -> bool:
4    if not root:
5      return True
6
7    def is_mirror(t1, t2):
8      if not t1 and not t2:
9        return True
10      if not t1 or not t2 or t1.val != t2.val:
11        return False
12      return is_mirror(t1.left, t2.right) and is_mirror(t1.right, t2.left)
13
14    return is_mirror(root.left, root.right)