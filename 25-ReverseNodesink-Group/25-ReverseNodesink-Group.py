# Last updated: 8/24/2026, 8:49:16 AM
1class Solution:
2
3  def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
4    if not head or not head.next or k == 0:
5      return head
6
7    length = 1
8    tail = head
9    while tail.next:
10      tail = tail.next
11      length += 1
12
13    k = k % length
14    if k == 0:
15      return head
16
17    tail.next = head
18
19    steps_to_new_tail = length - k
20    new_tail = head
21    for _ in range(steps_to_new_tail - 1):
22      new_tail = new_tail.next
23
24    new_head = new_tail.next
25    new_tail.next = None
26
27    return new_head