# Last updated: 8/24/2026, 9:12:41 AM
1from collections import deque
2
3
4class Solution:
5
6  def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
7    res = []
8    queue = deque([root])
9
10    while queue:
11      level_sum = 0
12      level_count = len(queue)
13
14      for _ in range(level_count):
15        node = queue.popleft()
16        level_sum += node.val
17        if node.left:
18          queue.append(node.left)
19        if node.right:
20          queue.append(node.right)
21
22      res.append(level_sum / level_count)
23
24    return res