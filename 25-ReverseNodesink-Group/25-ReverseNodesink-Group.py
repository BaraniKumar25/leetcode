# Last updated: 8/24/2026, 9:11:27 AM
1class Solution:
2
3  def countNodes(self, root: Optional[TreeNode]) -> int:
4    if not root:
5      return 0
6
7    left_height = self._get_left_height(root.left)
8    right_height = self._get_left_height(root.right)
9
10    if left_height == right_height:
11      return (1 << left_height) + self.countNodes(root.right)
12    else:
13      return (1 << right_height) + self.countNodes(root.left)
14
15  def _get_left_height(self, node: Optional[TreeNode]) -> int:
16    height = 0
17    while node:
18      height += 1
19      node = node.left
20    return height