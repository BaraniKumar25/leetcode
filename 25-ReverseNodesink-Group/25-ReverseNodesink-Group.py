# Last updated: 8/24/2026, 8:48:53 AM
1class Solution:
2
3  def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
4    dummy = ListNode(0, head)
5    prev = dummy
6
7    while head:
8      if head.next and head.val == head.next.val:
9        while head.next and head.val == head.next.val:
10          head = head.next
11        prev.next = head.next
12      else:
13        prev = prev.next
14      head = head.next
15
16    return dummy.next