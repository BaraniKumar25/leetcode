# Last updated: 8/24/2026, 8:58:44 AM
1class BSTIterator:
2
3  def __init__(self, root: Optional[TreeNode]):
4    self.stack = []
5    self._push_left(root)
6
7  def _push_left(self, node):
8    while node:
9      self.stack.append(node)
10      node = node.left
11
12  def next(self) -> int:
13    top_node = self.stack.pop()
14    if top_node.right:
15      self._push_left(top_node.right)
16    return top_node.val
17
18  def hasNext(self) -> bool:
19    return len(self.stack) > 0