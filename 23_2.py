from typing import List, Optional
from heapq import heappush, heappop


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Using Heap Solution
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        data = []
        head = tmp = ListNode()
        for item in range(len(lists)):
            # 중복 에러를 피하기 위해 인덱스를 함께 입력 -> 비교군은 val 값이므로 val값이 제일 앞으로 들어와야함
            heappush(data, (lists[item].val, item, lists[item]))

        while data:
            node = heappop(data)
            idx = node[2]
            tmp.next = node[1]

            tmp = tmp.next

            if tmp.next:
                heappush(data, (tmp.next.val, idx, tmp.next))

        return head.next

