# Last updated: 8/24/2026, 9:12:19 AM
1class Solution:
2
3  def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
4    res = []
5
6    def dfs(node, depth):
7      if not node:
8        return
9
10      if depth == len(res):
11        res.append(node.val)
12
13      dfs(node.right, depth + 1)
14      dfs(node.left, depth + 1)
15
16    dfs(root, 0)
17    return res