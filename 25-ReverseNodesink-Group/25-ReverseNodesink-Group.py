# Last updated: 8/24/2026, 9:30:19 AM
1class Solution:
2
3  def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
4    stack = []
5    curr = root
6
7    while curr or stack:
8      while curr:
9        stack.append(curr)
10        curr = curr.left
11
12      curr = stack.pop()
13      k -= 1
14      if k == 0:
15        return curr.val
16
17      curr = curr.right