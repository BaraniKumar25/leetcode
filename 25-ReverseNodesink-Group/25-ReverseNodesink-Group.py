# Last updated: 8/24/2026, 8:53:13 AM
1class Solution:
2
3  def buildTree(
4      self, preorder: List[int], inorder: List[int]
5  ) -> Optional[TreeNode]:
6    inorder_map = {val: idx for idx, val in enumerate(inorder)}
7    pre_idx = 0
8
9    def helper(left, right):
10      nonlocal pre_idx
11      if left > right:
12        return None
13
14      root_val = preorder[pre_idx]
15      root = TreeNode(root_val)
16      pre_idx += 1
17
18      mid = inorder_map[root_val]
19      root.left = helper(left, mid - 1)
20      root.right = helper(mid + 1, right)
21
22      return root
23
24    return helper(0, len(inorder) - 1)