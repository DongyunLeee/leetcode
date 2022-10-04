from typing import List
import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        heap = []
        ret = list()

        for item in cnt:
            heapq.heappush(heap, (-cnt[item], item))

        for _ in range(k):
            ret.append(heapq.heappop(heap)[1])

        return ret