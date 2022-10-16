from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def DFS(path, index):
            ret.append(path[:])

            for i in range(index, len(nums)):
                DFS(path + [nums[i]], i + 1)

        ret = list()
        DFS([], 0)
        return ret