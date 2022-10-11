from typing import List

# dfs 알고리즘을 이용한 풀이임
# 리스트 카피본을 만들어 dfs 알고리즘을 재귀하는 방식
# 비효율적으로 느껴지며 개선된 dfs 풀이방식이 있을 것으로 판단됨
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(num: int, comb: int, lists: list):
            if comb == k:
                ret.append(lists)
                return

            for item in range(num, n + 1):
                cp_list = lists[:]
                cp_list.append(item)
                dfs(item + 1, comb + 1, cp_list)

        ret = list()
        dfs(1, 0, [])

        return ret