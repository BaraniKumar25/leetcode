# Last updated: 8/24/2026, 9:27:04 AM
1from collections import deque
2
3
4class Solution:
5
6  def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
7    if not root:
8      return []
9
10    res = []
11    queue = deque([root])
12
13    while queue:
14      level = []
15      for _ in range(len(queue)):
16        node = queue.popleft()
17        level.append(node.val)
18
19        if node.left:
20          queue.append(node.left)
21        if node.right:
22          queue.append(node.right)
23
24      res.append(level)
25
26    return res