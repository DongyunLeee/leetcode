from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = list()
        prev_items = list()

        def dfs(items: list):
            if len(items) == 0:
                ret.append(prev_items[:])

            for i in items:
                next_items = items[:]
                next_items.remove(i)

                prev_items.append(i)
                dfs(next_items)
                prev_items.remove(i)

        dfs(nums)

        return ret