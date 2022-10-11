from typing import List

# dfs 알고리즘을 이용한 풀이임
# 기존 리스트를 복사하는 방식이 아닌 함수동작 후, 리스트에서 해당값을 다시 반환하는 방식으로 진행
# run time 및 Memory에서 개선점 확인
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(num: int, comb: int, lists: list):
            if comb == k:
                ret.append(lists[:]) # 리스트의 값[:]만 복사
                return

            for item in range(num, n + 1):
                lists.append(item)
                dfs(item + 1, comb + 1, lists)
                lists.pop()

        ret = list()
        dfs(1, 0, [])

        return ret