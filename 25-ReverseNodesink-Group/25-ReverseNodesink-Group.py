# Last updated: 8/24/2026, 8:48:28 AM
1class Solution:
2
3  def removeNthFromEnd(
4      self, head: Optional[ListNode], n: int
5  ) -> Optional[ListNode]:
6    dummy = ListNode(0, head)
7    fast = head
8    slow = dummy
9
10    for _ in range(n):
11      fast = fast.next
12
13    while fast:
14      fast = fast.next
15      slow = slow.next
16
17    slow.next = slow.next.next
18
19    return dummy.next