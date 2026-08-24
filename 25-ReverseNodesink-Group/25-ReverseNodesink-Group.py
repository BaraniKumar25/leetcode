# Last updated: 8/24/2026, 8:55:34 AM
1class Solution:
2
3  def flatten(self, root: Optional[TreeNode]) -> None:
4    curr = root
5
6    while curr:
7      if curr.left:
8        prev = curr.left
9        while prev.right:
10          prev = prev.right
11
12        prev.right = curr.right
13        curr.right = curr.left
14        curr.left = None
15
16      curr = curr.right