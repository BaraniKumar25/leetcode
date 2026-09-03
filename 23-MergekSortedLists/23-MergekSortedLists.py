# Last updated: 9/3/2026, 2:00:34 PM
1class Solution:
2    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
3        dummy = ListNode(0, head)
4        prev, curr = dummy, head
5
6        while curr and curr.next:
7            nxtPair = curr.next.next
8            second = curr.next
9
10            # Swap the pair
11            second.next = curr
12            curr.next = nxtPair
13            prev.next = second
14
15            # Update pointers
16            prev = curr
17            curr = nxtPair
18
19        return dummy.next