# Last updated: 8/24/2026, 8:54:31 AM
1class Solution:
2
3  def buildTree(
4      self, inorder: List[int], postorder: List[int]
5  ) -> Optional[TreeNode]:
6    inorder_map = {val: idx for idx, val in enumerate(inorder)}
7    post_idx = len(postorder) - 1
8
9    def helper(left, right):
10      nonlocal post_idx
11      if left > right:
12        return None
13
14      root_val = postorder[post_idx]
15      root = TreeNode(root_val)
16      post_idx -= 1
17
18      mid = inorder_map[root_val]
19      root.right = helper(mid + 1, right)
20      root.left = helper(left, mid - 1)
21
22      return root
23
24    return helper(0, len(inorder) - 1)