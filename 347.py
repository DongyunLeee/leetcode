from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ret = {}
        result = []
        for item in nums:
            if item not in ret:
                ret[item] = 1
            else:
                ret[item] += 1

        result = sorted(ret, key=lambda x:ret[x], reverse=True)

        return result[:k]