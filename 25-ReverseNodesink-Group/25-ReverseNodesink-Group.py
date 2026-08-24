# Last updated: 8/24/2026, 8:48:04 AM
1class Solution:
2
3  def reverseKGroup(
4      self, head: Optional[ListNode], k: int
5  ) -> Optional[ListNode]:
6    dummy = ListNode(0, head)
7    group_prev = dummy
8
9    while True:
10      kth = self.get_kth(group_prev, k)
11      if not kth:
12        break
13
14      group_next = kth.next
15      prev, curr = kth.next, group_prev.next
16
17      while curr != group_next:
18        tmp = curr.next
19        curr.next = prev
20        prev = curr
21        curr = tmp
22
23      tmp = group_prev.next
24      group_prev.next = kth
25      group_prev = tmp
26
27    return dummy.next
28
29  def get_kth(self, curr, k):
30    while curr and k > 0:
31      curr = curr.next
32      k -= 1
33    return curr