# Last updated: 8/24/2026, 8:46:54 AM
1class Solution:
2
3  def reverseBetween(
4      self, head: Optional[ListNode], left: int, right: int
5  ) -> Optional[ListNode]:
6    if not head or left == right:
7      return head
8
9    dummy = ListNode(0, head)
10    prev = dummy
11
12    for _ in range(left - 1):
13      prev = prev.next
14
15    curr = prev.next
16
17    for _ in range(right - left):
18      temp = curr.next
19      curr.next = temp.next
20      temp.next = prev.next
21      prev.next = temp
22
23    return dummy.next