# Last updated: 8/24/2026, 9:29:20 AM
1from collections import deque
2
3
4class Solution:
5
6  def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
7    if not root:
8      return []
9
10    res = []
11    queue = deque([root])
12    left_to_right = True
13
14    while queue:
15      level_size = len(queue)
16      level = deque()
17
18      for _ in range(level_size):
19        node = queue.popleft()
20
21        if left_to_right:
22          level.append(node.val)
23        else:
24          level.appendleft(node.val)
25
26        if node.left:
27          queue.append(node.left)
28        if node.right:
29          queue.append(node.right)
30
31      res.append(list(level))
32      left_to_right = not left_to_right
33
34    return res