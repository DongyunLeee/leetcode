from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def DFS(key):
            while path[key]:
                DFS(path[key].pop(0))
            route.append(key)

        path = defaultdict(list)
        for key, val in sorted(tickets):
            path[key].append(val)

        route = list()
        DFS("JFK")

        route.reverse()
        return route