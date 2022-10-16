from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def DFS(nums, number):
            if number == target:
                # 리스트 정렬을 통해 중복된 조합을 체크
                nums.sort()
                if nums not in ret:
                    ret.append(nums[:])
                return

            for item in candidates:
                if number + item > target:
                    continue
                prev_nums = nums[:]
                prev_number = number
                prev_number += item
                prev_nums.append(item)
                DFS(prev_nums, prev_number)

        ret = list()
        DFS([], 0)
        return ret
