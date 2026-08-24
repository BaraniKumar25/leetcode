# Last updated: 8/24/2026, 9:29:37 AM
1class Solution:
2
3  def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
4    min_diff = float('inf')
5    prev = None
6
7    def inorder(node):
8      nonlocal min_diff, prev
9      if not node:
10        return
11
12      inorder(node.left)
13
14      if prev is not None:
15        min_diff = min(min_diff, node.val - prev)
16      prev = node.val
17
18      inorder(node.right)
19
20    inorder(root)
21    return min_diff