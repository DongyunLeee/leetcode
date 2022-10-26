from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def DFS(item):
            # 순환구조인 경우, False
            if item in traced:
                return False
            # 이미 방문한 경우, Ture
            if item in visit:
                return True

            traced.add(item)
            for target in graph[item]:
                if not DFS(target):
                    return False

            # 탐색 종료 후 해당 노드 제거
            traced.remove(item)
            # 탐색 종료 후 방문 노드에 추가
            visit.add(item)

            return True

        graph = defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)

        traced = set() # 순환노드
        visit = set() # 방문노드

        # 순환 구조 판별
        for x in list(graph):
            if not DFS(x):
                return False

        return True
