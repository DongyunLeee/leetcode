from typing import List


# DFS 알고리즘을 이용한 해결방법(재귀적 방법)
class Solution:
    def dfs(self, grid: List[List[str]], x: int, y: int):
        # 유효한 리스트인가 체크
        if x < 0 or x >= len(grid) or \
                y < 0 or y >= len(grid[0]) or \
                grid[x][y] != '1':
            return

        # 방문한 리스트는 방문처리('0')를 하고 동서남북을 다시 방문
        grid[x][y] = '0'
        self.dfs(grid, x - 1, y)
        self.dfs(grid, x, y - 1)
        self.dfs(grid, x, y + 1)
        self.dfs(grid, x + 1, y)

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        cnt = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '1':
                    cnt += 1
                    self.dfs(grid, x, y)

        return cnt
