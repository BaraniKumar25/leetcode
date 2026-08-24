# Last updated: 8/24/2026, 8:50:06 AM
1class Node:
2
3  def __init__(self, key: int, val: int):
4    self.key = key
5    self.val = val
6    self.prev = None
7    self.next = None
8
9
10class LRUCache:
11
12  def __init__(self, capacity: int):
13    self.cap = capacity
14    self.cache = {}
15    self.head = Node(0, 0)
16    self.tail = Node(0, 0)
17    self.head.next = self.tail
18    self.tail.prev = self.head
19
20  def _remove(self, node: Node):
21    prev, nxt = node.prev, node.next
22    prev.next = nxt
23    nxt.prev = prev
24
25  def _add(self, node: Node):
26    prev, nxt = self.tail.prev, self.tail
27    prev.next = node
28    node.prev = prev
29    node.next = nxt
30    nxt.prev = node
31
32  def get(self, key: int) -> int:
33    if key in self.cache:
34      node = self.cache[key]
35      self._remove(node)
36      self._add(node)
37      return node.val
38    return -1
39
40  def put(self, key: int, value: int) -> None:
41    if key in self.cache:
42      self._remove(self.cache[key])
43
44    node = Node(key, value)
45    self._add(node)
46    self.cache[key] = node
47
48    if len(self.cache) > self.cap:
49      lru = self.head.next
50      self._remove(lru)
51      del self.cache[lru.key]