# Last updated: 8/24/2026, 8:49:41 AM
1class Solution:
2
3  def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
4    before_head = ListNode(0)
5    after_head = ListNode(0)
6
7    before = before_head
8    after = after_head
9
10    while head:
11      if head.val < x:
12        before.next = head
13        before = before.next
14      else:
15        after.next = head
16        after = after.next
17      head = head.next
18
19    after.next = None
20    before.next = after_head.next
21
22    return before_head.next