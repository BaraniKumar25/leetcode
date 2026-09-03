# Last updated: 9/3/2026, 1:59:45 PM
1import heapq
2
3class Solution:
4    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
5        heap = []
6        
7        # Push the head of each non-empty list into the min-heap
8        for i, node in enumerate(lists):
9            if node:
10                heapq.heappush(heap, (node.val, i, node))
11                
12        dummy = ListNode(0)
13        current = dummy
14        
15        while heap:
16            val, i, node = heapq.heappop(heap)
17            current.next = node
18            current = current.next
19            
20            if node.next:
21                heapq.heappush(heap, (node.next.val, i, node.next))
22                
23        return dummy.next