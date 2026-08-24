# Last updated: 8/24/2026, 8:46:09 AM
1class Solution:
2
3  def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
4    if not head:
5      return None
6
7    old_to_new = {}
8
9    curr = head
10    while curr:
11      old_to_new[curr] = Node(curr.val)
12      curr = curr.next
13
14    curr = head
15    while curr:
16      old_to_new[curr].next = old_to_new.get(curr.next)
17      old_to_new[curr].random = old_to_new.get(curr.random)
18      curr = curr.next
19
20    return old_to_new[head]